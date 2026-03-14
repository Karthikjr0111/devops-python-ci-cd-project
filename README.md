# DevOps Python CI/CD Project

## Overview

This project demonstrates a complete DevOps workflow for a Python application including automated testing, CI/CD pipeline automation, and Docker containerization.

The goal of the project is to show how a developer can push code to GitHub and automatically trigger a CI pipeline that tests and validates the application.

---

## Tech Stack

* Python
* Flask
* Pytest
* Git
* GitHub
* GitHub Actions
* Docker

---

## Project Structure

devops-python-ci-cd-project
│
├── .github/workflows/ci.yml   # CI pipeline configuration
├── app/                       # Python application
├── tests/                     # Automated tests
├── Dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore rules

---

## Run Locally

Install dependencies

pip install -r requirements.txt

Run the application

python app/app.py

Open in browser

http://localhost:5000

---

## Run with Docker

Build Docker image

docker build -t devops-python-app .

Run container

docker run -p 5000:5000 devops-python-app

---

## CI/CD Pipeline

The project uses GitHub Actions for Continuous Integration.

Whenever code is pushed to the main branch, the pipeline:

1. Checks out the repository
2. Sets up Python environment
3. Installs dependencies
4. Runs automated tests

This ensures that every code change is validated automatically.

---

## Learning Outcome

Through this project I learned:

* Setting up GitHub repositories and version control
* Writing automated tests using Pytest
* Creating CI pipelines with GitHub Actions
* Containerizing applications using Docker
* Structuring a professional DevOps project repository
