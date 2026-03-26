import boto3

# 1. Start
s3 = boto3.client('s3')

# 2. Define the "Recovery Mission"
bucket_name = 'morke-cloud-lab-123'
object_name = 'secret_note.txt'
output_name = 'recovered_note.txt'

# 3. Perform the Download
print(f"Attempting to recover {object_name} from {bucket_name}...")

try:
    s3.download_file(bucket_name, object_name, output_name)
    print(f"SUCCESS! File recovered as: {output_name}")
except Exception as e:
    print(f"Recovery Failed. Error: {e}")
