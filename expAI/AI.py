import json
import os


def check_json_file(json_string):
    try:
        y = json.loads(json_string)
        print(y)
    except ValueError as v:
        print('Lỗi cú pháp: ' + str(v))

    return False

def insert_into_result():
    

# x =  '{ "name":"John", "age":30,"city":"New York"}'
# check_json_file(x)