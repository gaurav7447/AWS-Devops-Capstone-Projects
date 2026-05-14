# 🚀 AWS Cost Optimization Automation using Lambda

## 📌 Overview
This project automates AWS cost optimization by identifying unused EC2 instances using AWS Lambda and CloudWatch.

---

## 🎯 Objective
Reduce AWS cost by detecting idle or stopped EC2 instances automatically.

---

## 🧰 AWS Services Used
- AWS Lambda
- Amazon CloudWatch
- Amazon EC2
- SNS (optional)

---

## ⚙️ Architecture
CloudWatch Trigger → Lambda → EC2 Check → Alert

---

## 🚀 Features
- Automated EC2 monitoring
- Cost optimization logic
- Serverless execution
- Scheduled monitoring

---

## ▶️ How it works
1. CloudWatch triggers Lambda every 5 minutes
2. Lambda checks EC2 instance states
3. Identifies stopped instances
4. Sends logs / alerts

---

## 💡 Future Improvements
- Auto-stop idle instances
- Budget alert integration
- Cost prediction model
- Auto tagging system

---

## 👨‍💻 Author
Gaurav Deshmane
AWS DevOps Learning Project