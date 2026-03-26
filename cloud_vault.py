import boto3

# 1. Connect to the S3 "Service"
s3 = boto3.resource('s3')

# 2. show all the buckets
print("Checking your Cloud Vault...")

for bucket in s3.buckets.all():
    print(f"Found Bucket: {bucket.name}")
import boto3

s3 = boto3.resource('s3')

# 1. List the Buckets
print("--- Your Cloud Vaults ---")
for bucket in s3.buckets.all():
    print(f"Vault Name: {bucket.name}")

    # 2.List the files inside EACH bucket
    print(f"  Contents of {bucket.name}:")
    for obj in bucket.objects.all():
        print(f"    - Found File: {obj.key}")
