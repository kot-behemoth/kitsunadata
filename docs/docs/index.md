---
title: Welcome
---

# Kitsuna Data


## About The Project

This is a concept for what a Rails-inspired small data platform for startups and SMEs could look like. After using a variety of end-to-end solutions like DOMO, Keboola, Mozart Data and others, I keep wishing there was something that would do the 80% of ELT + BI out-of-the-box, without the price surprises.

This project is an attempt to stitch together a set of solid and reliable open-source tools that combine into a lean platform where one data engineer can own the entire lifecycle. From ELT, to data modelling, to deploying and scaling in production.

!!! warning

    The project is very much in the pre-alpha stage. This is more of an experiment and is not meant for produciton workloads.

### Main Features

1. **🧪 From laptop to production in minutes** - Develop locally with DuckDB, deploy with the same code. No more "it works on my machine" problems.

1. **⚡ Lightning-fast analytics on any data size** - DuckDB's column-oriented design handles gigabytes of data on modest hardware. Query billions of rows in seconds.

1. **📊 Beautiful dashboards** - Drag-and-drop dataviz with Metabase. Perfect for everyone - tech and non-tech alike.

1. **💸 Scale without breaking the bank** - Enterprise-grade data stack for as little as $30/month. DuckDB + SQLMesh's efficiency means less compute costs than Snowflake or BigQuery.

1. **🔄 30+ ready-to-use integrations** - Instant integrations with dlt for Stripe, GitHub, Salesforce, and more. Connect your SaaS tools with minimal code.

1. **🤖 Just ask your DB** - Ask questions in plain English with DuckDB's MCP. Get immediate answers without writing complex queries.

1. **🔍 End-to-end data lineage** - SQLMesh tracks transformations from raw to gold data. Understand exactly where metrics come from and debug easily.

### Goals

- Local-first development for the entire stack.
- Support companies that can't afford heavy, expensive data tools or large teams.
- No "SSO tax" - all tools should be either fully free, or affordable once deployed in serious prod use case.
- No k8s, so a small data team can be self-sufficient .
- Cheap path to production and scaling.

### Tech Stack

- _Extract_ (planned): [dlt](https://dlthub.com/)
- Transform: [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/)
- Data Storage: [DuckDB](https://duckdb.org/)
- BI / data viz: [Metabase](https://www.metabase.com/)
- Deployment: [Dokku](https://dokku.com/docs/getting-started/install/digitalocean.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
