import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = f"/tmp/{key.split('/')[-1]}"
    upload_path = f"/tmp/resized-{key.split('/')[-1]}"

    # Download image
    s3.download_file(bucket_name, key, download_path)

    # Resize image
    size = (300, 300)

    with Image.open(download_path) as image:
        image = image.resize(size)
        image.save(upload_path)

    # Upload back to S3 (output folder)
    s3.upload_file(
        upload_path,
        bucket_name,
        f"output/resized-{key.split('/')[-1]}"
    )

    return {
        "statusCode": 200,
        "body": "Image resized successfully!"
    }