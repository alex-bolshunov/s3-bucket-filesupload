from pydoc import cli
import boto3
from dotenv import load_dotenv
from os import getenv
from upload_download import push

print("Executing...")


#gets credentials
load_dotenv()

#get path, endpoint_url, bucket_name
path = getenv('DIRECTORY_PATH')
endpoint_url = getenv('ENDPOINT_URL')
bucket_name = getenv('BUCKET_NAME')

# s3 client
client = boto3.client('s3', endpoint_url = endpoint_url)

# #upoad files
status = push(path, bucket_name, client)

if status: print('Files have been uploaded')
else: print('Smth went wrong')