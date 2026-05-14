#!/bin/bash

# ===============================
# AWS EC2 Setup Script
# Flask App Deployment
# ===============================

echo "🚀 Updating system packages..."
sudo yum update -y

echo "🐍 Installing Python3..."
sudo yum install -y python3

echo "📦 Installing pip..."
sudo yum install -y python3-pip

echo "📁 Creating application directory..."
mkdir -p /home/ec2-user/app
cd /home/ec2-user/app

echo "📥 Installing Python dependencies..."
pip3 install flask mysql-connector-python gunicorn

echo "📝 Creating Flask application..."

cat > app.py <<EOF
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 AWS Scalable Web App Running Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

echo "▶️ Starting Flask application..."
nohup python3 app.py > app.log 2>&1 &

echo "✅ Installation completed successfully!"