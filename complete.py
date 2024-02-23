"""
@filename:SuperContext.py
@author:张晓锋
@time:-02-19
"""
import json
import os
filename = './Hateful_complete.json'
prompt = []
info = []
temp = {}
count = 0
with open('./Hateful_caption.json')as fp1:
    question_data = json.load(fp1)
with open('./Hateful_OCR1.json')as fp2:
    answer_data = json.load(fp2)
#question_data = json.loads('./TextVQA_0.5.1_test.json')
#answer_data = json.loads('./textVQA_test_images.json')
for question in question_data:
    for answer in answer_data:
        if question['image'][:-4] == answer['image_id']:
            temp["image_id"] = question['image']
            temp["caption"] = question['description']
            temp["OCR_result"] = answer['OCR_result']
            print(temp)
            count = count+1
            #temp["OCR_result"] = answer['OCR_result']
            info.append(temp.copy())
print(count)
with open(filename, 'w') as file:
    json.dump(info, file)