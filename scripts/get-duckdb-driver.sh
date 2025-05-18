#!/bin/bash
set -e

# The release version to get
DUCKDB_DRIVER_VERSION="0.3.0"

# Create drivers directory if it doesn't exist
mkdir -p drivers

# Download DuckDB driver for Metabase
echo "Downloading DuckDB driver for Metabase version ${DUCKDB_DRIVER_VERSION}..."
curl -L -o drivers/duckdb.metabase-driver.jar https://github.com/motherduckdb/metabase_duckdb_driver/releases/download/${DUCKDB_DRIVER_VERSION}/duckdb.metabase-driver.jar

# Set appropriate permissions
chmod 644 drivers/duckdb.metabase-driver.jar

echo "DuckDB driver version ${DUCKDB_DRIVER_VERSION} downloaded successfully to drivers/duckdb.metabase-driver.jar"
