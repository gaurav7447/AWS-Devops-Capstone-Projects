#!/bin/bash

ACCOUNT_ID=597809152772
REGION=ap-south-1

echo "Pushing image to ECR..."
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/flask-app:latest