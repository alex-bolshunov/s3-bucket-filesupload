import boto3
from pprint import pprint

from dotenv import load_dotenv

ENDPOINT_URL = 'https://s3.us-west-004.backblazeb2.com'
BUCKET_NAME = 'test-for-andrei'
OBJECT_NAME = 'hello.txt'

#gets credentials
load_dotenv()

client = boto3.client('s3', endpoint_url=ENDPOINT_URL)

# client.put_object(Bucket = BUCKET_NAME, Key = OBJECT_NAME, Body = 'hello'.encode()) #putting an object into a bucket
response = client.get_object(Bucket = BUCKET_NAME, Key = OBJECT_NAME) #getting an object from a bucket 

pprint(response['Body'].read().decode())