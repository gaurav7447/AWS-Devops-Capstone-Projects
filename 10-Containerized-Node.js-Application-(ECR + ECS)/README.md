# Containerized Node.js Application using AWS ECS

## Technologies Used

- Node.js
- Docker
- AWS ECR
- AWS ECS Fargate

## Features

- Containerized Node.js application
- Docker image pushed to Amazon ECR
- Deployed using ECS Fargate

## Steps

1. Create Node.js app
2. Dockerize application
3. Push image to ECR
4. Deploy container on ECS

## Output

Application successfully deployed on AWS ECS.

## Architecture

Node.js App
    ↓
Docker Container
    ↓
Amazon ECR (stores image)
    ↓
Amazon ECS Fargate (runs container)
    ↓
Public IP → Browser Access
