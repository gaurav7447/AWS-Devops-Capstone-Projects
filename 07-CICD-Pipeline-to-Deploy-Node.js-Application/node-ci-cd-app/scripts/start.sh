#!/bin/bash

cd /home/ec2-user/app

echo "Installing dependencies..."
npm install

echo "Starting application..."
node app.js