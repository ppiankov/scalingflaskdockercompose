###### Scalable Web Server Deployment and Monitoring with Docker Compose

## Overview
This repository provides a demonstration of a scalable web server environment using Docker Compose. It features a Dockerized Flask application with Nginx as a reverse proxy, handling dynamic scaling based on load via an external Python script. A Grafana dashboard is set up to monitor the system using Prometheus metrics, providing insights into the application's performance.

## Note: 
The scaling_script2.py included is for demonstration purposes to illustrate an approach to handling dynamic scaling.

## Prerequisites
Docker and Docker Compose installed
Python for the scaling script
Access to a Linux environment

## Getting Started
To deploy and test the scalable Flask application, follow these steps:

## 1. Clone the Repository
Clone this repository to your local machine:


git clone https://github.com/ppiankov/scalingflaskdockercompose

cd scalingflaskdockercompose

## 2. Start the Application
Run Docker Compose to start the services:


docker-compose up --build

## 3. Run the Scaling Script
In a separate terminal, start the scaling script to dynamically adjust the number of Flask instances based on load:


bash run_scaling.sh

## 4. Generate Load
To see the scaling in action, generate load using a tool like Siege:


siege -c 20 -t 2M http://localhost:5000/status
Replace localhost with your server's IP address if accessing from a different machine.

## 5. Monitoring and Metrics
Access the following endpoints to monitor the application and view metrics:

Flask Application Endpoint:

Working location: http://localhost:5000/status
Metrics: http://localhost:5000/metrics
Prometheus:

Targets: http://localhost:9090/targets
Grafana Dashboard:

Dashboard: http://localhost:3000/d/_eX4mpl3/flask-dashboard

## Documentation

For more detailed information about the configuration and components used in this project, 
refer to the individual configuration files and script comments within the repository.