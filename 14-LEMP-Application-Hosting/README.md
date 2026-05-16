# ⚡ LEMP Application Hosting on AWS EC2

This project demonstrates how to deploy a modern LEMP Stack Application on AWS using an EC2 instance.

LEMP stands for:

- **L** → Linux  
- **E** → Nginx  
- **M** → MySQL  
- **P** → PHP  

The application is hosted on an Ubuntu EC2 server using Nginx as the web server, PHP for backend scripting, and MySQL as the database server.

---

# 📌 Project Objective

The main objective of this project is to:

- Launch and configure an AWS EC2 instance
- Install and configure Nginx Web Server
- Install MySQL Database Server
- Install PHP and PHP-FPM
- Configure Nginx with PHP
- Deploy a PHP application on AWS

---

# 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Linux (Ubuntu) | Operating System |
| Nginx | Web Server |
| MySQL | Database Server |
| PHP | Backend Scripting |
| PHP-FPM | PHP Process Manager |
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
                │ Ubuntu Linux Server │
                └──────────┬──────────┘
                           │
         ┌──────────────────────────────────┐
         │            LEMP STACK            │
         │                                  │
         │   Nginx Web Server               │
         │   PHP Application                │
         │   PHP-FPM Service                │
         │   MySQL Database                 │
         └──────────────────────────────────┘
```

---

# ⚙️ AWS Services Used

- Amazon EC2
- Security Groups
- Elastic IP (Optional)

---

# 📂 Project Structure

```text
14-LEMP-Application-Hosting/
│
├── index.php
├── README.md
└── screenshots/
    ├── 01-nginx-working.png
    ├── 02-lemp-ui.png
    ├── 03-nginx-status.png
    ├── 04-php-version.png
    └── 05-ec2-running.png
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

## 2️⃣ Install Nginx

```bash
sudo apt install nginx -y
```

Start and enable Nginx:

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
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

## 4️⃣ Install PHP & PHP-FPM

```bash
sudo apt install php-fpm php-mysql -y
```

Check PHP version:

```bash
php -v
```

---

## 5️⃣ Configure Nginx

Create configuration file:

```bash
sudo nano /etc/nginx/sites-available/lemp-app
```

Enable configuration:

```bash
sudo ln -s /etc/nginx/sites-available/lemp-app /etc/nginx/sites-enabled/
```

Remove default configuration:

```bash
sudo rm /etc/nginx/sites-enabled/default
```

---

## 6️⃣ Deploy PHP Application

Create application directory:

```bash
sudo mkdir -p /var/www/lemp-app
```

Create PHP file:

```bash
nano /var/www/lemp-app/index.php
```

Restart services:

```bash
sudo systemctl restart nginx
sudo systemctl restart php8.5-fpm
```

---

# 🌐 Application Output

Access application using:

```text
http://YOUR_PUBLIC_IP
```

The application displays a modern LEMP Stack hosting page running successfully on AWS EC2.

---

# 📸 Screenshots

| Screenshot | Description |
|---|---|
| Nginx Working | Nginx default page |
| EC2 Running | Running EC2 instance |
| PHP Version | PHP installation verification |
| Nginx Status | Web server status |
| Final Output | Hosted LEMP application |

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

- Linux server basics
- Nginx web hosting
- PHP-FPM configuration
- MySQL installation and setup
- AWS EC2 management
- Modern cloud application hosting

---

# 📌 Future Improvements

- Use Amazon RDS instead of local MySQL
- Add SSL/HTTPS
- Configure Domain Name
- Deploy Laravel Application
- Add Load Balancer
- Enable Auto Scaling
- Create CI/CD Pipeline

---

# 👨‍💻 Author

**Gaurav Deshmane**

AWS & DevOps Project