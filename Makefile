.PHONY: download-duckdb-driver generate-test-project

download-duckdb-driver:
	./scripts/get-duckdb-driver.sh

generate-test-project:
	rm -rf test-gen-project && \
	. .venv/bin/activate && \
	copier copy template ./ --data project_name="test-gen-project" --data project_description="Test project"
