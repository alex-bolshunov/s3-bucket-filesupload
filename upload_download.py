from local import get_all_files

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
    status = 'success'
    local_files = get_local_file_names(path)
    files_to_upload = get_unique_names(local_files, get_bucket_file_names(bucket_name, client)) if not overwrite else local_files
    files_uploaded = []
    number_of_files = 0

    
    try:
        for file_name in files_to_upload:
            client.upload_file(path + '\\' + f'\\{file_name}', bucket_name, file_name)
            files_uploaded.append(file_name)
            number_of_files += 1

    except:
        status = 'abort'

    return { 'status': status, 'number_of_files': number_of_files, 'local_files': local_files, 'files_uploaded': files_uploaded}
