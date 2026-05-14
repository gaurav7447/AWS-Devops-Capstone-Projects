# 🚀 AWS Static Website Hosting Automation using Python (Boto3)

## 📌 Overview
This project automates deployment of a static website using AWS S3 and Python (boto3).

Instead of manually uploading files, the script:
- Creates S3 bucket
- Enables static hosting
- Uploads website files
- Generates live URL

---

## 🧰 AWS Services Used
- Amazon S3
- boto3 (AWS SDK for Python)

---

## 🚀 Features
- Fully automated deployment
- No AWS Console required
- Static website hosting on S3
- Public access configuration

---

## 📁 Project Structure
- website/ → HTML & CSS files
- upload_script/ → automation script
- requirements.txt

---

## ⚙️ Setup

```bash
pip install boto3
aws configure