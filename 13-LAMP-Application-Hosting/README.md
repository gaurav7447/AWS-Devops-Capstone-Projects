# 🚀 LAMP Application Hosting on AWS EC2

This project demonstrates how to deploy a LAMP Stack Application on AWS using an EC2 instance.

LAMP stands for:

- **L** → Linux  
- **A** → Apache  
- **M** → MySQL  
- **P** → PHP  

The application is hosted on an Ubuntu EC2 server with Apache as the web server, PHP for backend scripting, and MySQL as the database server.

---

# 📌 Project Objective

The main objective of this project is to:

- Launch and configure an AWS EC2 instance
- Install Apache Web Server
- Install and configure MySQL
- Install PHP and required modules
- Deploy a PHP application on AWS
- Understand basic cloud hosting concepts

---

# 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Linux (Ubuntu) | Operating System |
| Apache2 | Web Server |
| MySQL | Database Server |
| PHP | Backend Scripting |
| AWS EC2 | Cloud Hosting |

---

# 🏗️ Architecture Diagram

```text
                ┌─────────────────────┐
                │     User Browser    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   AWS EC2 Instance  │
                │  Ubuntu Linux Server│
                └──────────┬──────────┘
                           │
          ┌────────────────────────────────┐
          │          LAMP STACK            │
          │                                │
          │  Apache Web Server             │
          │  PHP Application               │
          │  MySQL Database                │
          └────────────────────────────────┘
```

---

# ⚙️ AWS Services Used

- Amazon EC2
- Security Groups
- Elastic IP (Optional)

---

# 📂 Project Structure

```text
13-LAMP-Application-Hosting/
│
├── index.php
├── README.md
└── screenshots/
    ├── 01-apache-working.png
    ├── 02-lamp-ui.png
    ├── 03-ec2-running.png
    ├── 04-apache-status.png
    └── 05-php-version.png
```

---

# 🖥️ EC2 Configuration

| Setting | Value |
|---|---|
| AMI | Ubuntu Server 24.04 LTS |
| Instance Type | t2.micro |
| Web Server Port | 80 |
| SSH Port | 22 |

---

# 🔐 Security Group Rules

| Type | Port |
|---|---|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |

---

# 🚀 Installation Steps

## 1️⃣ Update Server

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2️⃣ Install Apache

```bash
sudo apt install apache2 -y
```

Start Apache:

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

---

## 3️⃣ Install MySQL

```bash
sudo apt install mysql-server -y
```

Secure MySQL:

```bash
sudo mysql_secure_installation
```

---

## 4️⃣ Install PHP

```bash
sudo apt install php libapache2-mod-php php-mysql -y
```

Check PHP version:

```bash
php -v
```

---

## 5️⃣ Deploy PHP Application

Move to web root directory:

```bash
cd /var/www/html
```

Remove default Apache page:

```bash
sudo rm index.html
```

Create PHP application:

```bash
sudo nano index.php
```

---

# 🌐 Application Output

Access application using:

```text
http://YOUR_PUBLIC_IP
```

The application displays a custom LAMP Stack hosting page running successfully on AWS EC2.

---

# 📸 Screenshots

| Screenshot | Description |
|---|---|
| Apache Working | Apache default page |
| EC2 Running | Running EC2 instance |
| PHP Version | PHP installation verification |
| Final Output | Hosted LAMP application |

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

- Linux server basics
- Apache web hosting
- MySQL installation and configuration
- PHP deployment
- AWS EC2 management
- Cloud application hosting

---

# 📌 Future Improvements

- Use Amazon RDS instead of local MySQL
- Add SSL/HTTPS
- Configure Domain Name
- Deploy Dynamic CRUD Application
- Add Load Balancer
- Enable Auto Scaling

---

# 👨‍💻 Author

**Gaurav Deshmane**

AWS & DevOps Project