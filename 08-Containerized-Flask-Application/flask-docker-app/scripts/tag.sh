#!/bin/bash

ACCOUNT_ID=597809152772
REGION=ap-south-1

echo "Tagging Docker image..."
docker tag flask-app:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/flask-app:latest