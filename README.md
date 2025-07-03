<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template"> -->
  <!--   <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  <!-- </a> -->

  <h3 align="center">Kitsuna Data</h3>

  <p align="center">
    Self-hosted one-person data platform
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#main-features">Main Features</a></li>
        <li><a href="#goals">Goals</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#inspiration">Inspiration</a></li>
  </ol>
</details>

## About The Project

This is a concept for what a Rails-inspired small data platform for startups and SMEs could look like. After using a variety of end-to-end solutions like DOMO, Keboola, Mozart Data and others, I keep wishing there was something that would do the 80% of ELT + BI out-of-the-box, without the price surprises.

This project is an attempt to stitch together a set of solid and reliable open-source tools that combine into a lean platform where one data engineer can own the entire lifecycle. From ELT, to data modelling, to deploying and scaling in production.

![Kitsuna overview diagram](docs/docs/assets/Overview.png)

### Main Features

1. **🧪 From laptop to production in minutes** - Develop locally with DuckDB, deploy with the same code. No more "it works on my machine" problems.

1. **⚡ Lightning-fast analytics on any data size** - DuckDB's column-oriented design handles gigabytes of data on modest hardware. Query billions of rows in seconds.

1. **📊 Beautiful dashboards** - Drag-and-drop dataviz with Metabase. Perfect for everyone - tech and non-tech alike.

1. **💸 Scale without breaking the bank** - Enterprise-grade data stack for as little as $30/month. DuckDB + SQLMesh's efficiency means less compute costs than Snowflake or BigQuery.

1. **🔄 30+ ready-to-use integrations** - Instant integrations with dlt for Stripe, GitHub, Salesforce, and more. Connect your SaaS tools with minimal code.

1. **🤖 Just ask your DB** - Ask questions in plain English with DuckDB's MCP. Get immediate answers without writing complex queries.

1. **🔍 End-to-end data lineage** - SQLMesh tracks transformations from raw to gold data. Understand exactly where metrics come from and debug easily.

> [!CAUTION]
> The project is very much in the pre-alpha stage. This is more of an experiment and is not meant for produciton workloads.

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
- Deployment: [Dokploy](https://dokploy.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* `uv`
* `mise` (recommended)
* `claude` (recommended)

### Installation

1. Clone this repository
2. Download the DuckDB driver for Metabase:
   ```bash
   make download-duckdb-driver
   ```
3. Start the services:
   ```bash
   docker-compose up -d
   ```
4. Access Metabase at http://localhost:3000

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Deployment

This project can be deployed to DigitalOcean/Hetzner/EC2 using Dokploy with the following architecture:

1. **Metabase Container**:
   - Dedicated hostname (e.g., metabase.yourdomain.com)
   - Access to mounted DuckDB volume

2. **dlt + SQLMesh Container**:
   - Combined container for data processing
   - Access to the same DuckDB volume

3. **Shared Storage**:
   - Used for persistent DuckDB storage

## Roadmap

- [x] Add SQLMesh
- [x] Add MCP for DuckDB
- [ ] Add dlt
    - [ ] Implement as an example: [Exploring StarCraft 2 data with Airflow, DuckDB and Streamlit \| by Volker Janz \| Data Engineer Things](https://blog.det.life/exploring-starcraft-2-data-with-airflow-duckdb-and-streamlit-7c0ad79f9ca6)
- [x] Add Dokku deployment configuration
    - [ ] Create a DigitalOcean box for a public demo
- [ ] Add installation docs
- [ ] Add usage docs
- [ ] Add Aider docs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Greg Goltsov - [@gregoltsov](https://x.com/gregoltsov), [gregoltsov.bsky.social](https://bsky.app/profile/gregoltsov.bsky.social).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Inspiration

Here are some projects which inspired my thinking and this project:

* [Modern Data Stack in a Box with DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
* [MDS-in-a-box: Monte Carlo simulation of the NBA season](https://github.com/matsonj/nba-monte-carlo)
* [Exploring StarCraft 2 data with Airflow, DuckDB and Streamlit](https://blog.det.life/exploring-starcraft-2-data-with-airflow-duckdb-and-streamlit-7c0ad79f9ca6)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
