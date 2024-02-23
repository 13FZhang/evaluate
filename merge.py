"""
@filename:merge.py
@author:张晓锋
@time:-02-20
"""
import json
temp = {}
info = []
filename = './textVQA_info.json'
with open('./textVQA_test_OCR.json')as fp1:
    data1 = json.load(fp1)
with open('./textVQA_test_caption.json')as fp2:
    data2 = json.load(fp2)
#question_data = json.loads('./TextVQA_0.5.1_test.json')
#answer_data = json.loads('./textVQA_test_images.json')
for i in data2:
    for j in data1:
        if i['image'] == j['image']:
            temp["image_id"] = i['image']
            temp["description"] = i['description']
            temp["OCR_result"] = j['OCR_result']
            info.append(temp.copy())
print(info)
with open(filename, 'w') as file:
    json.dump(info, file)