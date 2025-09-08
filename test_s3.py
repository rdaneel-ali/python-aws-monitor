import boto3
import os

s3 = boto3.client(
    "s3",
    endpoint_url=f"http://{os.getenv('LOCALSTACK_HOST')}:{os.getenv('EDGE_PORT')}"
)

s3.create_bucket(Bucket="my-test-bucket")
print("Buckets:", s3.list_buckets())
