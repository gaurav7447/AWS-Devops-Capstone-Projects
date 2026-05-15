# 7️⃣ CI/CD Pipeline to Deploy Node.js Application

## 📌 Overview

This project demonstrates a **CI/CD (Continuous Integration / Continuous Deployment) pipeline** to automatically build and deploy a Node.js application whenever code is pushed to the repository.

The pipeline ensures faster releases, reduced manual effort, and consistent deployments.

---

## 🎯 Purpose

- Automatically build and deploy application on every code change
- Reduce manual deployment efforts
- Improve development speed and reliability
- Maintain consistent deployment process

---

## 🧰 AWS Services Used

- AWS CodePipeline → Orchestrates the CI/CD workflow
- AWS CodeBuild → Builds and tests the application
- Amazon EC2 / S3 → Deployment target (host application)

---

## 🏗️ Architecture Flow
itHub / CodeCommit
↓
AWS CodePipeline
↓
AWS CodeBuild (Build & Test)
↓
Deploy Stage
↓
EC2 Instance / S3 Bucket
