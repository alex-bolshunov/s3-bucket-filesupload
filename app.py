from pydoc import cli
import boto3
import sys
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

#get overwrite
overwrite =  sys.argv[1].lower() == 'true' if len(sys.argv) > 1 else False

#upoad files
try:
    push(path, bucket_name, client, overwrite)
    print('Files have been uploaded')
except: 
    print('Smth went wrong')

