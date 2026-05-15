#!/bin/bash

echo "Forcing ECS deployment..."

aws ecs update-service \
  --cluster flask-cluster \
  --service flask-service \
  --force-new-deployment \
  --region ap-south-1