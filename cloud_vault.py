import boto3

# 1. Connect to the S3 "Service"
s3 = boto3.resource('s3')

# 2. AWS to show all the buckets
print("Checking your Cloud Vault...")

for bucket in s3.buckets.all():
    print(f"Found Bucket: {bucket.name}")
