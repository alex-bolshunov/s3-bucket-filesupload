import boto3

from dotenv import load_dotenv

ENDPOINT_URL = 'https://s3.us-west-004.backblazeb2.com'
BUCKET_NAME = 'test-for-andrei'
OBJECT_NAME = 'hello.txt'

#gets credentials
load_dotenv()

client = boto3.client('s3', endpoint_url=ENDPOINT_URL)
