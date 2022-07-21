import boto3
import os


def s3_connection():
    try:
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="",
            aws_secret_access_key="",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3


s3 = s3_connection()

""" Upload Test """
# try:
#     s3.upload_file("./tmp/test.jpg", "42brick-s3", "tmp/test.jpg")
# except Exception as e:
#     print(e)
# else:
#     print("upload is completed")

""" Download Test """
# try:
#     s3.download_file("42brick-s3", "test.jpg", "test.jpg")
# except Exception as e:
#     print(e)
# else:
#     print("download is completed")

""" Download ALL Test """
# s3_contents = s3.list_objects(Bucket="42brick-s3")["Contents"]
# for s3_key in s3_contents:
#     s3_object = s3_key['Key']
#     val = s3_object.find("/")
#     if val == -1:
#         s3.download_file("42brick-s3", s3_object, s3_object)
#     else:
#         rep = s3_object[:3]
#         if not os.path.exists(rep):
#             os.makedirs(rep)
#         s3.download_file("42brick-s3", s3_object, s3_object)

"""Delete Test """
response = s3.delete_object(Bucket="42brick-s3", Key="test.jpg")
print(response)
