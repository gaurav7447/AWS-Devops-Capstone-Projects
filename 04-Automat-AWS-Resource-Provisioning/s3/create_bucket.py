import boto3

s3 = boto3.client('s3')

bucket_name = "my-aws-automation-bucket-12345"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created:", bucket_name)