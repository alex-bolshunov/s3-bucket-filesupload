from msilib.schema import Error
from botocore.exceptions import ClientError
import logging
from os import path
from local import get_all_files

def upload_file(file_name, bucket_name, client, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None: object_name = path.basename(file_name)

    # Upload the file
    try: client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#returns list of the names from the specified bucket, returns empty list if no files
def get_bucket_file_names(bucket_name, client):
    files = client.list_objects(Bucket=bucket_name)
    return list(map(lambda object: object['Key'], files["Contents"])) if "Contents" in files else []

#returns the list of the names in a specified directory
def get_local_file_names(path):
    return get_all_files(path)

#returns unique values only
def get_unique_names(local_files, cloud_files):
    return list(set(local_files) - set(cloud_files))


#upload files to the bucket
def push(path, bucket_name, client, overwrite = False):
    status = True
    local_files = get_local_file_names(path)

    files_to_upload = get_unique_names(local_files, get_bucket_file_names(bucket_name, client)) if not overwrite else local_files

    try:
        for file_name in files_to_upload:
            upload_file(path + '\\' + f'\\{file_name}', bucket_name, client, file_name)
    except Error:
        status = False
    return status
