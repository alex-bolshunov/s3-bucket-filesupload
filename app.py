import boto3
from aifc import Error
from sys import argv
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
overwrite =  'overwrite' in argv

#upoad files
try:
    response = push(path, bucket_name, client, overwrite)
    print(f'Operation status: {response["status"]}\nNumber of files uploaded: {response["number_of_files"]}\nFiles uploaded: {response["files_uploaded"]}')
except Error as err:
    print('Smth went wrong')
    print(err)
