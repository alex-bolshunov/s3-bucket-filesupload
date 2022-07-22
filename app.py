import boto3
from upload import upload_file
from dotenv import load_dotenv
from os import getenv
from directory import get_all_files

ENDPOINT_URL = 'https://s3.us-west-004.backblazeb2.com'
BUCKET_NAME = 'test-for-andrei'

def push(path):
    files = get_all_files(path)
    for file_name in files:
        upload_file(path + '\\' + f'\\{file_name}', BUCKET_NAME, client, file_name)

    return len(files) > 0

#gets credentials
load_dotenv()

#get path
path = getenv('DIRECTORY_PATH') #+ '\\' + '\\test.txt'

#s3 client
client = boto3.client('s3', endpoint_url=ENDPOINT_URL)

status = push(path)

if status: print('Files are uploaded')
else: print('Smth went wrong')