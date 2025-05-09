<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template"> -->
  <!--   <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  <!-- </a> -->

  <h3 align="center">Kitsuna Data</h3>

  <p align="center">
    The one person data and BI platform
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
        <li><a href="#goals">Goals</a></li>
        <li><a href="#tech-choices">Tech Choices</a></li>
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

### Goals

- Local-first development for the entire stack.
- Support companies that can't afford heavy, expensive data tools or large teams.
- No "SSO tax" - all tools should be either fully free, or affordable once deployed in serious prod use case.
- No k8s, so a small data team can be self-sufficient .
- Cheap path to production and scaling.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tech Choices

- Extraction. [dlt]()
- Transform. [SQLMesh]()
- BI / data viz (planned). [Metabase]()
- Deployment (planned). [kamal]()

## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* `uv`
* `mise` (recommended)
* `claude` (recommended)

### Installation

TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

TODO

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] Add SQLMesh
- [x] Add MCP for DuckDB
- [ ] Add dlt
    - [ ] Implement as an example: [Exploring StarCraft 2 data with Airflow, DuckDB and Streamlit \| by Volker Janz \| Data Engineer Things](https://blog.det.life/exploring-starcraft-2-data-with-airflow-duckdb-and-streamlit-7c0ad79f9ca6)
- [ ] Add Kamal for prod deployment
    - [ ] Create a Hetzner box for a public demo
- [ ] Add installation docs
- [ ] Add usage docs
- [ ] Add Aider docs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Greg Goltsov - [@gregoltsov](https://x.com/gregoltsov), [gregoltsov.bsky.social](https://bsky.app/profile/gregoltsov.bsky.social) - greg@goltsov.info.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Inspiration

Here are some projects which inspired my thinking and this project:

* [Modern Data Stack in a Box with DuckDB](https://duckdb.org/2022/10/12/modern-data-stack-in-a-box.html)
* [MDS-in-a-box: Monte Carlo simulation of the NBA season](https://github.com/matsonj/nba-monte-carlo)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
