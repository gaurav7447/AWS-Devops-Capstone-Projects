# Scalable Web App on AWS (NLB + Auto Scaling)

## Overview
This project demonstrates a scalable and highly available web application deployed on AWS using EC2, Network Load Balancer, and Auto Scaling Groups.

## Architecture
- Network Load Balancer distributes traffic
- Auto Scaling Group manages EC2 instances
- Flask application runs on each EC2 instance

## AWS Services Used
- EC2
- Network Load Balancer (NLB)
- Auto Scaling Group
- VPC & Security Groups

## How it works
1. User hits NLB endpoint
2. Traffic is distributed to EC2 instances
3. Auto Scaling increases/decreases instances based on load

## Features
- High Availability
- Auto Scaling
- Load Balancing
- Fault Tolerance

## Deployment Steps
1. Create Launch Template
2. Create Auto Scaling Group
3. Attach Network Load Balancer
4. Configure Security Groups
5. Deploy Flask App via User Data Script

## Output
Application is accessible via NLB DNS name.
