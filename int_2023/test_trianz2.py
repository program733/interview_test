print('test trianz l2...')


# scenario , dag should download data from s3 and process and place into bq

from boto3 import bot3
import pandas

Acess_key= 'asdfasdf'
access_token = 'asdfasdfasdf'
region = 'east-u1'

boto_client = boto3.s3.client(access_token=access_token,acces_key = access_key,region=region)

file = boto_client.download(path = 'path')

data = pd.read_csv(file)

