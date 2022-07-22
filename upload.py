from msilib.schema import Error
from botocore.exceptions import ClientError
import logging
from os import path
from directory import get_all_files

def upload_file(file_name, bucket_name, client, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None: object_name = path.basename(file_name)

    # Upload the file
    try: client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def push(path, bucket_name, client):
    files = get_all_files(path)
    status = True
    try:
        for file_name in files:
            upload_file(path + '\\' + f'\\{file_name}', bucket_name, client, file_name)
    except Error as err:
        status = False

    return status