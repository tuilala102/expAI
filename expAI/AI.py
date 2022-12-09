import json
import os


def check_json_file(json_string):
    try:
        y = json.loads(json_string)
        return True
    except ValueError as v:
        print('Lỗi cú pháp: ' + str(v))
        return False