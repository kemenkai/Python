import time
# import datetime
# import boto3
import boto.s3.connection
from boto3.session import Session

access_key = 'S7BQDCHX99G7H3YDX0EX'
secret_key = 'w6rnLjMp529FRrtb3Ds6YE51sTjiwe6sALAdOYuS'
conn = boto.connect_s3(aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key,
                       host="192.168.8.106",
                       port=7480,
                       is_secure=False,
                       calling_format=boto.s3.connection.OrdinaryCallingFormat())

# bucket = conn.create_bucket("test4")
# startTime2 = time.time()
# for bucket in conn.get_all_buckets():
#     print("{name}\t{created}".format(name=bucket.name, created=bucket.creation_date))
# endTime2 = time.time()
# print("date: {0} ms".format((endTime2 - startTime2) * 1000))


# startTime = datetime.datetime.now()
# for bucket in conn.get_all_buckets():
#     print("{name}\t{created}".format(name=bucket.name, created=bucket.creation_date))
# endTime = datetime.datetime.now()
# print(endTime - startTime)


session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
url = "http://192.168.8.106:7480"
# s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, endpoint_url=url)
ceph_client = session.client('s3', endpoint_url=url)
ceph_resource = session.resource('s3', endpoint_url=url)
# resp = ceph_client.put_object(Bucket="test1", Key="tmpWeb.config", Body=open('D:\\tmpWeb.config','rb').read())
# print(resp)

startTime = time.time()
ceph_resource.meta.client.upload_file("d:\\一份脱敏记录.xml", "test1", "一份脱敏记录.xml")
endTime = time.time()
print("Upload 725KB File Time: {0} ms".format((endTime - startTime) * 1000))

startTime = time.time()
ceph_resource.meta.client.upload_file("d:\\最大入院记录.xml", "test1", "最大入院记录.xml")
endTime = time.time()
print("Upload 5.88MB File Time: {0} ms".format((endTime - startTime) * 1000))

startTime = time.time()
ceph_resource.meta.client.upload_file("d:\\88.9MB.zip", "test1", "88.9MB.zip")
endTime = time.time()
print("Upload 88.9MB File Time: {0} ms \n".format((endTime - startTime) * 1000))

response = ceph_client.list_objects(Bucket='test1')
for tmp in response['Contents']:
    print("Object: {0}".format(tmp['Key']))

print("\n")

startTime = time.time()
download_fle = ceph_resource.meta.client.download_file("test1", "一份脱敏记录.xml", "d:\\tmp\\一份脱敏记录_ceph1.xml")
endTime = time.time()
print("Download 725KB File Time: {0} ms".format((endTime - startTime) * 1000))

startTime = time.time()
ceph_resource.meta.client.download_file("test1", "最大入院记录.xml", "d:\\tmp\\最大入院记录1.xml")
endTime = time.time()
print("Download 5.88MB File Time: {0} ms".format((endTime - startTime) * 1000))

startTime = time.time()
ceph_resource.meta.client.download_file("test1", "88.9MB.zip", "d:\\tmp\\88.9MB_1.zip")
endTime = time.time()
print("Download 88.9mb File Time: {0} ms".format((endTime - startTime) * 1000))

ceph_client.delete_object(Bucket="test1", Key="一份脱敏记录.xml")
ceph_client.delete_object(Bucket="test1", Key="最大入院记录.xml")
ceph_client.delete_object(Bucket="test1", Key="88.9MB.zip")

try:
    response = ceph_client.list_objects(Bucket='test1')
    for tmp in response['Contents']:
        print("Delete to Object: {0}".format(tmp['Key']))
except Exception:
    print("List Object Null")
