# SNS Setup for Cost Optimizer Project

## 🎯 Purpose
Send email alerts when AWS resources are detected as idle or stopped.

---

## 🧰 AWS Service Used
Amazon SNS (Simple Notification Service)

---

## 🚀 Steps to Create SNS Topic

### 1. Create Topic
- Go to AWS SNS Console
- Click "Create topic"
- Type: Standard
- Name: cost-optimizer-alerts

---

### 2. Create Subscription
- Protocol: Email
- Endpoint: your-email@gmail.com
- Confirm email from inbox

---

### 3. Add Permission to Lambda

Attach this policy to Lambda role:
- sns:Publish

---

## 📌 SNS Topic ARN Example
arn:aws:sns:ap-south-1:123456789012:cost-optimizer-alerts

---

## 🚀 How it works
Lambda detects idle EC2 → SNS sends email alert