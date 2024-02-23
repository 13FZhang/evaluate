"""
@filename:convert.py
@author:张晓锋
@time:-02-19
"""
import ast
import json
dirt = {}
list = []
filename = './Hateful_OCR1.json'
with open('./Hateful_OCR.json')as fp2:
    info = json.load(fp2)
for i in info:
    dirt["image_id"] = i[7:i.index(".")]
    dirt["OCR_result"] = i[i.index("O")+12:]
    list.append(dirt.copy())
    print(dirt)
with open(filename, 'w') as file:
    json.dump(list, file)
    #print(json_dirt)