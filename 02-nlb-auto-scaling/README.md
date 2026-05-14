# 2️⃣ Scalable Web App with NLB and Auto Scaling

## Project Overview

This project demonstrates deployment of a scalable and high-performance web application on AWS using:

- EC2
- Network Load Balancer (NLB)
- Auto Scaling Group

The architecture automatically distributes traffic across multiple EC2 instances and scales infrastructure based on demand.

---

## AWS Services Used

- Amazon EC2
- Network Load Balancer (NLB)
- Auto Scaling Group (ASG)
- Launch Templates
- Amazon Machine Image (AMI)
- Security Groups
- Amazon VPC

---

## Architecture

Users → NLB → Auto Scaling Group → EC2 Instances

---

## Features

- High performance load balancing
- Low latency traffic handling
- Dynamic scaling
- Fault tolerance
- Health checks
- High availability

---

## Steps Performed

- Created EC2 web server
- Installed Apache Web Server
- Configured dynamic Instance ID display
- Created custom AMI
- Created Launch Template
- Configured TCP-based Target Group
- Configured Network Load Balancer
- Configured Auto Scaling Group
- Tested load balancing
- Tested scaling activity

---

## Learning Outcome

- Learned Network Load Balancer concepts
- Learned Layer 4 load balancing
- Learned Auto Scaling
- Understood scalable architecture
- Worked with TCP health checks
- Learned EC2 bootstrapping using User Data
- Learned AWS Metadata Service (IMDSv2)

---

## Author

Gaurav Deshmane
