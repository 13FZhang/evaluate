"""
@filename:count.py
@author:张晓锋
@time:-02-20
"""
import json
count1 = 0
count2 = 0
count3 = 0
with open('./Hateful_OCR.json')as fp1:
    question_data = json.load(fp1)
with open('./Hateful_caption.json')as fp2:
    answer_data = json.load(fp2)
with open('./Hateful_complete.json')as fp3:
    answer_data1 = json.load(fp3)
for i in question_data:
    count1 = count1+1
for j in answer_data:
    count2 = count2+1
for k in answer_data1:
    count3 = count3 +1
print(count1)
print(count2)
print(count3)