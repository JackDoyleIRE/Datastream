<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

 <a href="https://github.com/github_username/repo_name">
    <img src="/images/stream.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Streaming Data Infrastructure</h3>

  <p align="center">
    Creating a custom distributed data infrastructure to generate and consume streaming data
    <br />
    <a href="https://github.com/JackDoyleIRE/Datastream"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JackDoyleIRE/Datastream">View Demo</a>
    ·
    <a href="https://github.com/JackDoyleIRE/Datastream/issues">Report Bug</a>
    ·
    <a href="https://github.com/JackDoyleIRE/Datastream/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Welcome to my custom data infrastructure project, a locally deployable solution designed for learning and experimentation in the realm of streaming data. This initiative harnesses the power of Docker to orchestrate multiple services seamlessly. At the heart of our system is the Flask App service, providing a RESTful API for generating and serving streaming data. Apache Beam, a versatile stream processing tool, takes center stage for data processing and analysis. Complementing these, Apache Flink acts as a robust stream processing framework, executing data processing jobs, while Redis serves as a reliable data store and message broker. This setup empowers users to build, monitor, and scale their streaming data applications efficiently. Whether you're a student, developer, or data enthusiast, this project provides an ideal environment for hands-on exploration and experimentation. To dive into this innovative data infrastructure, follow our simple setup instructions below and explore the capabilities of this locally deployable solution.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the app and how to install them (mac only).
* python
  ```sh
  brew install python
  ```
* docker
  ```sh
  brew install docker
  ```

### Installation

2. Clone the repo
   ```sh
   git clone https://github.com/JackDoyleIRE/Datastream.git
   ```
3. Build the docker image
   ```sh
   docker-compose build
   ```
4. Run the docker image
   ```sh
   docker-compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

App currently in development.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Implement the flink service as a runner for beam 
- [ ] Extend the apache beam code
- [ ] Deploy to a local kubernetes environment
- [ ] Try Kafka as the message que
- [ ] Add a local Terraform setup
- [ ] Link with CGP for cloud deployment

See the [open issues](https://github.com/JackDoyleIRE/Datastream/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

