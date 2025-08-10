import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')
bucket = "my-bucket"
prefix = "raw-data/"

def archive_old_data(days=30):
    cutoff = datetime.utcnow() - timedelta(days=days)
    objs = s3.list_objects_v2(Bucket=bucket, Prefix=prefix).get("Contents", [])
    for obj in objs:
        if obj["LastModified"].replace(tzinfo=None) < cutoff:
            print(f"Archiving: {obj['Key']}")
            s3.copy_object(
                Bucket=bucket,
                CopySource={"Bucket": bucket, "Key": obj["Key"]},
                Key="archive/" + obj["Key"]
            )
            s3.delete_object(Bucket=bucket, Key=obj["Key"])

if __name__ == "__main__":
    archive_old_data(60)
