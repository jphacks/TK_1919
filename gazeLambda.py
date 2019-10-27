import os
import sys
import time
import json
import base64
import math
from botocore.vendored import requests

def lambda_handler(event, context):
    
    endPoint = 'http://a8b88762ef01211e9950f0eacce6e863-2021028779.ap-northeast-1.elb.amazonaws.com'      
    proxies = []
    url = endPoint + "/v1/query/gaze"
    reqPara = {
        'file_b64' : event['b64']
    }
    params = {}
    headers = {'Content-Type' : 'application/json'}
    data = json.dumps(reqPara).encode('utf-8')
    res = requests.post(url, params=params, data=data, headers=headers, proxies=proxies, timeout=10)
    
    return {
        'statusCode': 200,
        'body': [res.json(),event['pictureNumber'],event['tryNumber']]
    }
