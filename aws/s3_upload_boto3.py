import boto3

def upload_file_to_s3(local_file, bucket, s3_key):
    s3 = boto3.client('s3')
    s3.upload_file(local_file, bucket, s3_key)
    print(f"Uploaded {local_file} to s3://{bucket}/{s3_key}")

if __name__ == "__main__":
    upload_file_to_s3("local_file.txt", "my-bucket", "remote_file.txt")
