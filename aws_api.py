import boto3
from pprint import pprint

s3_instance = boto3.client('s3')
iam_inst = boto3.client('iam')


users = iam_inst.list_users()
# pprint(users)
for user in users['Users']:
    print(user['UserName'])
    print("****************")