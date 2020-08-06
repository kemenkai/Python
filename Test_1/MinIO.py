import time
from minio import Minio
from minio.error import ResponseError

minio_client = Minio("192.168.8.106:9000",
                     access_key="AKIAIOSFODNN7EXAMPLE",
                     secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                     secure=False)


def upload(object_name, file_path):
    try:
        minio_client.fput_object("test1", object_name, file_path, content_type="application/text")
    except ResponseError as err:
        print(err.message)


def remove_object(objects):
    try:
        for del_err in minio_client.remove_objects("test1", objects):
            print("Remove Error: {}".format(del_err))
    except ResponseError as err:
        print(err.message)


def download_object(object_name, file_path):
    # Get a full object and prints the original object stat information.
    try:
        minio_client.fget_object('test1', object_name, file_path)
    except ResponseError as err:
        print(err.message)


objects_list = ["一份脱敏记录.xml", "最大入院记录.xml", "88.9MB.zip"]
for object_name_tmp in objects_list:
    startTime = time.time()
    upload(object_name_tmp, "D:\\{0}".format(object_name_tmp))
    endTime = time.time()
    print("Upload {1} File Time: {0} ms".format((endTime - startTime) * 1000, object_name_tmp))

print("\n")
list_objects = minio_client.list_objects("test1")
for tmp in list_objects:
    print("Bucket Name: {0}, Object Name: {1}".format(tmp.bucket_name, tmp.object_name))
print("\n")

for object_name_tmp in objects_list:
    startTime = time.time()
    download_object(object_name_tmp, "d:\\tmp\\{0}".format(object_name_tmp))
    endTime = time.time()
    print("Download {0} File Time: {1} ms".format(object_name_tmp, (endTime - startTime) * 1000))

remove_object(objects_list)
