import json
import os
from .models import *
import random


def check_json_file(json_string):
    try:
        y = json.loads(json_string)
        return True
    except ValueError as v:
        print('Lỗi cú pháp: ' + str(v))
        return False

def insert_to_result(id_para,index):
    try:
        new_result = Trainningresults()
        new_result.configid = Paramsconfigs.objects.get(pk=id_para)
        new_result.accuracy = random.randint(1, 100)
        new_result.lossvalue = random.randint(1, 100)
        new_result.trainresultindex = index
        new_result.save()
        return True
    except ValueError as e:
        print("error!!" + str(e))
        return False

# index = 1
# while True:
#     insert_to_result(5,index)
#     index +=1
#     if index == 10:
#         break

