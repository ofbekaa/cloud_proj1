import boto3

# This line connects script to the S3 service
s3 = boto3.client('s3')

#  BUCKET NAME HERE
target_bucket = 'morke-cloud-lab-123'
file_name = 'progress.txt'

print(f"Starting upload of {file_name}...")

# command that sends the file to the cloud
s3.upload_file(file_name, target_bucket, file_name)

print("Upload Successful!")

import boto3

# 1. connection to the S3 service
s3 = boto3.client('s3')

# 2. Define "
filename = 'secret_note.txt'
bucket_name = 'morke-cloud-lab-123'
object_name = 'secret_note.txt'

# 3. Perform the Upload
print(f"Uploading {filename} to {bucket_name}...")

try:
    s3.upload_file(filename, bucket_name, object_name)
    print("Upload Successful! Your file is in the Cloud Vault.")
except Exception as e:
    print(f"Upload Failed. Error: {e}")
