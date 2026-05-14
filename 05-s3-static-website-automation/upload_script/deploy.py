import boto3
import os

s3 = boto3.client('s3')

bucket_name = "gaurav-static-web-bucket-7447"

# 1. Create S3 bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created:", bucket_name)

# 2. Enable static website hosting
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'}
    }
)

print("Static website hosting enabled")

# 3. Upload files
folder = "website"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    s3.upload_file(
        file_path,
        bucket_name,
        file,
        ExtraArgs={'ContentType': 'text/html' if file.endswith('.html') else 'text/css'}
    )

    print("Uploaded:", file)

print("\n🎉 Website deployed successfully!")
print("URL: http://{}.s3-website.ap-south-1.amazonaws.com".format(bucket_name))