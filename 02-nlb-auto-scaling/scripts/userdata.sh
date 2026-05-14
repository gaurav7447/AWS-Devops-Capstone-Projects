#!/bin/bash

dnf update -y
dnf install httpd -y

systemctl start httpd
systemctl enable httpd

INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)

cat <<EOF > /var/www/html/index.html
<h1>NLB Scalable AWS Web App</h1>
<h2>Instance ID: $INSTANCE_ID</h2>
EOF