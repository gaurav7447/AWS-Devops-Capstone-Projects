#!/bin/bash

# Update system
yum update -y

# Install Python + tools
yum install -y python3 pip

# Install Apache (optional)
yum install -y httpd
systemctl start httpd
systemctl enable httpd

# Install Flask dependencies
pip3 install flask mysql-connector-python gunicorn

# Create app directory
mkdir -p /home/ec2-user/app
cd /home/ec2-user/app

# Create simple Flask app
cat > app.py <<EOF
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 AWS Scalable App Running Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

# Run app in background
nohup python3 app.py > app.log 2>&1 &