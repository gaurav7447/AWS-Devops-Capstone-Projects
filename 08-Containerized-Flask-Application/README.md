# 🐳 Containerized Flask Application (AWS ECS + ECR)

## 📌 Overview
This project demonstrates how to containerize a Flask application using Docker and deploy it on AWS using ECS Fargate and ECR.

---

## 🚀 Tech Stack
- Python (Flask)
- Docker
- AWS ECR
- AWS ECS (Fargate)

---

## 🏗️ Architecture
1. Flask App (Local)
2. Docker Image Build
3. Push Image to ECR
4. Deploy on ECS Fargate
5. Access via Public IP

---

## 📦 Deployment Steps

### 1. Build Docker Image
```bash
docker build -t flask-app .