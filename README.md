# DevOps Python CI/CD Project

## Overview
This project demonstrates a complete DevOps workflow for a Python application.

## Features
- Python API using Flask
- Automated testing with pytest
- CI pipeline using GitHub Actions
- Docker containerization

## Tech Stack
Python, Flask, Pytest, Git, GitHub, GitHub Actions, Docker

## Run Locally
pip install flask pytest  
python app/app.py

## Run with Docker
docker build -t devops-python-app .  
docker run -p 5000:5000 devops-python-app

## CI Pipeline
The CI pipeline automatically runs tests when code is pushed using GitHub Actions.