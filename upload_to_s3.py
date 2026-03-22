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
