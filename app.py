import boto3
from dotenv import load_dotenv
from os import getenv
from upload import push

#gets credentials
load_dotenv()

#get path, endpoint_url, bucket_name
path = getenv('DIRECTORY_PATH')
endpoint_url = getenv('ENDPOINT_URL')
bucket_name = getenv('BUCKET_NAME')

# s3 client
client = boto3.client('s3', endpoint_url = endpoint_url)

#upoad files
status = push(path, bucket_name, client)

if status: print('Files are uploaded')
else: print('Smth went wrong')