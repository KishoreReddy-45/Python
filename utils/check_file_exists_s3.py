import boto3

def check_file_exists(bucket, key):
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket, Key=key)
        print(f"✅ File exists: s3://{bucket}/{key}")
        return True
    except s3.exceptions.ClientError:
        print(f"❌ File NOT found: s3://{bucket}/{key}")
        return False

if __name__ == "__main__":
    check_file_exists("my-bucket", "data/2025-08-10/data.csv")
