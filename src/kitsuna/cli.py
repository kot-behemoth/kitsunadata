#!/usr/bin/env python3
"""Kitsuna CLI - Create and manage Kitsuna data platform projects."""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional
import click
import copier


@click.group()
@click.version_option()
def cli():
    """Kitsuna - Self-hosted one-person data platform.
    
    Create and manage data platform projects with DuckDB, SQLMesh, and Metabase.
    """
    pass


@cli.command()
@click.argument('project_name')
@click.option('--directory', '-d', default='.', help='Directory to create project in')
@click.option('--no-input', is_flag=True, help='Use default values without prompting')
def init(project_name: str, directory: str, no_input: bool):
    """Initialize a new Kitsuna project.
    
    Example:
        kitsuna init my-data-platform
    """
    template_path = Path(__file__).parent.parent.parent
    print(f"template_path={template_path}")
    assert False
    destination = Path(directory) / project_name
    
    if destination.exists():
        click.echo(f"Error: Directory '{destination}' already exists!", err=True)
        sys.exit(1)
    
    click.echo(f"🦊 Creating new Kitsuna project: {project_name}")
    
    try:
        # Use copier to create project from template
        copier.run_copy(
            str(template_path),
            str(destination),
            data={"project_name": project_name},
            unsafe=True,
            vcs_ref="HEAD",
            quiet=no_input
        )
        
        click.echo(f"✅ Project created successfully at: {destination}")
        click.echo("\n📋 Next steps:")
        click.echo(f"  1. cd {project_name}")
        click.echo("  2. make download-duckdb-driver")
        click.echo("  3. docker-compose up -d")
        click.echo("  4. Open http://localhost:3000 for Metabase")
        
    except Exception as e:
        click.echo(f"Error creating project: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('--detach', '-d', is_flag=True, help='Run containers in background')
def up(detach: bool):
    """Start all Kitsuna services."""
    if not Path("docker-compose.yml").exists():
        click.echo("Error: No docker-compose.yml found. Are you in a Kitsuna project?", err=True)
        sys.exit(1)
    
    cmd = ["docker-compose", "up"]
    if detach:
        cmd.append("-d")
    
    click.echo("🚀 Starting Kitsuna services...")
    subprocess.run(cmd)


@cli.command()
def down():
    """Stop all Kitsuna services."""
    if not Path("docker-compose.yml").exists():
        click.echo("Error: No docker-compose.yml found. Are you in a Kitsuna project?", err=True)
        sys.exit(1)
    
    click.echo("🛑 Stopping Kitsuna services...")
    subprocess.run(["docker-compose", "down"])


@cli.command()
def validate():
    """Validate project structure and configuration."""
    required_files = [
        "docker-compose.yml",
        "Makefile",
        "sqlmesh/config.yaml",
        "docker/Dockerfile.elt",
        "docker/Dockerfile.metabase"
    ]
    
    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)
    
    if missing:
        click.echo("❌ Missing required files:", err=True)
        for file in missing:
            click.echo(f"  - {file}", err=True)
        sys.exit(1)
    else:
        click.echo("✅ Project structure is valid!")


@cli.command()
def logs():
    """Show logs from all services."""
    if not Path("docker-compose.yml").exists():
        click.echo("Error: No docker-compose.yml found. Are you in a Kitsuna project?", err=True)
        sys.exit(1)
    
    subprocess.run(["docker-compose", "logs", "-f"])


if __name__ == "__main__":
    cli()
