from celery import shared_task
import os
import re
import json
import boto3
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()
# parse_srt  parses SRT FILE AND THAN CONVERT IT TO JSON (PYTHON DICT FORMAT)
def parse_srt(srt_string):
    srt_list = []

    for line in srt_string.split('\n\n'):
        if line != '':
            index = int(re.match(r'\d+', line).group())

            pos = re.search(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+',
                            line).end() + 1
            content = line[pos:]
            start_time_string = re.findall(
                r'(\d+:\d+:\d+,\d+) --> \d+:\d+:\d+,\d+', line)[0]
            end_time_string = re.findall(
                r'\d+:\d+:\d+,\d+ --> (\d+:\d+:\d+,\d+)', line)[0]
            start_time = start_time_string
            end_time = end_time_string

            srt_list.append({
                'index': index,
                'content': content,
                'start': start_time,
                'end': end_time
            })

    return srt_list

# CELERY TASK TO 
# 1) FETCH SRT FILE USING CCEXTRACTOR
# 2) CONVERT SRT TO JSON
# 3) UPLOAD SRT FILE TO DYNAMODB
# IT TAKES VIDEO_ID AND VIDEO_FILE NAME AS INPUT ARGUMENTS (CALLED WHEN FILE IS UPLOADED IN VIEWS.PY ADD FUNCTION

@shared_task(bind=True)
def fetchsrt(self, id, name):
    os.system(f'cmd /c "ccextractorwinfull {name}"')
    # removing and adding srt
    newname = name[:-4] + ".srt"
    srt = open(newname, 'r', encoding="utf-8").read()
    parsed_srt = parse_srt(srt)
    open("newFile.json", 'w', encoding="utf-8").write(
        json.dumps(parsed_srt, indent=2, sort_keys=True))

    # Working with DynamoDB

    dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'ap-south-1',  aws_access_key_id =env('aws_access_key_id'), aws_secret_access_key = env('aws_secret_access_key'))
    
    product_table = dynamo_client.Table('videoshare')
    file = open("newFile.json",'r')
    file = file.read()
    data_file = {'srt_id': str(id), "data": json.loads(file)}

    product_table.put_item(Item = data_file)
    os.remove("newFile.json")
    os.remove(name)
    os.remove(newname)

    return f'Done Fetching SRT for Video ID: {id}'