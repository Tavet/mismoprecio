import boto3
import json

def get_clothes_data(store_name):
    s3 = boto3.resource('s3')
    data = s3.Object('best-deal-stores-info',
                     'clothes/clothes.json').get()['Body'].read().decode('utf-8')
    json_data = json.loads(data)
    return [x for x in json_data if x['store'] == store_name][0]['content']
