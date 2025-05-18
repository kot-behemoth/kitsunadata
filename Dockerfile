FROM metabase/metabase:latest

# Create plugins directory if it doesn't exist
RUN mkdir -p /plugins

# Copy the DuckDB driver from the local drivers directory to the default plugins directory
COPY drivers/duckdb.metabase-driver.jar /plugins/
