import os
import paddlehub as hub

senta = hub.Module(name="senta_bilstm")

test_text = [
'''
輸入文字
'''
]

input_dict = {"text": test_text}

results = senta.sentiment_classify(data=input_dict)
for index, result in enumerate(results):
    
    print(test_text[index], result['sentiment_key'])
