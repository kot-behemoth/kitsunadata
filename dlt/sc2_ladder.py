import dlt
from dlt.sources.helpers import requests
import logging
from typing import Iterator, Dict, Any
import pendulum

logger = logging.getLogger(__name__)

# Configuration
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
BASE_URI = "https://eu.api.blizzard.com"
REGION_ID = 2  # Europe

# Create a configured requests client with retry logic
client = requests.Client(
    request_timeout=30,
    request_max_retries=4,
    request_backoff_factor=2,
)


@dlt.source(name="starcraft2")
def starcraft2_source():
    """Source for StarCraft 2 ladder data"""
    
    # Get access token
    token = get_access_token()
    
    # Return both resources
    return [
        grandmaster_ladder(token),
        player_profiles(token)
    ]


def get_access_token() -> str:
    """Obtain OAuth2 access token from Battle.net"""
    response = client.post(
        "https://oauth.battle.net/token",
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET)
    )
    response.raise_for_status()
    return response.json()["access_token"]


@dlt.resource(
    name="ladder",
    write_disposition="replace",
    primary_key="id"
)
def grandmaster_ladder(token: str) -> Iterator[Dict[str, Any]]:
    """Fetch and yield grandmaster ladder data"""
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get ladder data
    response = client.get(
        f"{BASE_URI}/sc2/ladder/grandmaster/{REGION_ID}",
        headers=headers
    )
    response.raise_for_status()
    
    ladder_teams = response.json().get("ladderTeams", [])
    
    # Process each team (filtering for solo players)
    for team in ladder_teams:
        if not team.get("teamMembers") or len(team["teamMembers"]) != 1:
            continue
            
        member = team["teamMembers"][0]
        
        # Extract base player data
        yield {
            "id": member["id"],
            "realm": member["realm"],
            "region": member["region"],
            "display_name": member["displayName"],
            "clan_tag": member.get("clanTag"),
            "favorite_race": member.get("favoriteRace"),
            "previous_rank": team["previousRank"],
            "points": team["points"],
            "wins": team["wins"],
            "losses": team["losses"],
            "mmr": team.get("mmr"),
            "join_timestamp": team["joinTimestamp"],
            "ingested_at": pendulum.now().isoformat()
        }


@dlt.resource(
    name="player_profiles",
    write_disposition="replace",
    primary_key="id"
)
def player_profiles(token: str) -> Iterator[Dict[str, Any]]:
    """Fetch player profile metadata for all ladder players"""
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # First, get all players from the ladder
    response = client.get(
        f"{BASE_URI}/sc2/ladder/grandmaster/{REGION_ID}",
        headers=headers
    )
    response.raise_for_status()
    
    ladder_teams = response.json().get("ladderTeams", [])
    
    # Extract unique players
    players = []
    for team in ladder_teams:
        if team.get("teamMembers") and len(team["teamMembers"]) == 1:
            member = team["teamMembers"][0]
            players.append({
                "id": member["id"],
                "realm": member["realm"],
                "region": member["region"]
            })
    
    # Fetch profile metadata for each player
    for i, player in enumerate(players, start=1):
        logger.info(f"Fetching profile metadata for player {i}/{len(players)}")
        
        try:
            metadata_response = client.get(
                f"{BASE_URI}/sc2/metadata/profile/{player['region']}/{player['realm']}/{player['id']}",
                headers=headers
            )
            
            if metadata_response.status_code == 200:
                metadata = metadata_response.json()
                yield {
                    "id": player["id"],
                    "realm": player["realm"],
                    "region": player["region"],
                    "profile_url": metadata.get("profileUrl"),
                    "avatar_url": metadata.get("avatarUrl"),
                    "name": metadata.get("name"),
                    "fetched_at": pendulum.now().isoformat()
                }
            else:
                logger.warning(f"Failed to fetch metadata for player {player['id']}: HTTP {metadata_response.status_code}")
                yield {
                    "id": player["id"],
                    "realm": player["realm"],
                    "region": player["region"],
                    "profile_url": None,
                    "avatar_url": None,
                    "name": None,
                    "fetched_at": pendulum.now().isoformat(),
                    "error": f"HTTP {metadata_response.status_code}"
                }
                
        except Exception as e:
            logger.error(f"Exception fetching metadata for player {player['id']}: {e}")
            yield {
                "id": player["id"],
                "realm": player["realm"],
                "region": player["region"],
                "profile_url": None,
                "avatar_url": None,
                "name": None,
                "fetched_at": pendulum.now().isoformat(),
                "error": str(e)
            }


def run_pipeline():
    """Run the dlt pipeline to load StarCraft 2 data into DuckDB"""
    
    # Configure the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="starcraft2_ladder",
        destination=dlt.destinations.duckdb("sc2data.db"),
        dataset_name="sc2_data"
    )
    
    # Run the pipeline
    info = pipeline.run(starcraft2_source())
    
    # Print load info
    print(info)
    
    # Show the loaded data
    with pipeline.sql_client() as client:
        ladder_count = client.execute_sql("SELECT COUNT(*) as count FROM ladder")[0][0]
        profile_count = client.execute_sql("SELECT COUNT(*) as count FROM player_profiles")[0][0]
        print(f"Loaded {ladder_count} ladder entries and {profile_count} player profiles")
        
        # Example query joining both tables
        print("\nTop 5 players with profile data:")
        results = client.execute_sql("""
            SELECT 
                l.display_name,
                l.points,
                l.mmr,
                p.name,
                p.profile_url
            FROM ladder l
            LEFT JOIN player_profiles p ON l.id = p.id
            ORDER BY l.points DESC
            LIMIT 5
        """)
        for row in results:
            print(f"  {row[0]} - Points: {row[1]}, MMR: {row[2]}, Name: {row[3]}")


if __name__ == "__main__":
    run_pipeline()
