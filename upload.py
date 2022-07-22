from botocore.exceptions import ClientError
import logging
from os import path

def upload_file(file_name, bucket, client, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None: object_name = path.basename(file_name)

    # Upload the file
    try: client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

