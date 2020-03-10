# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」

import os
type_in = input("input:")
judge_flag=False
path = os.path.join(os.path.abspath('.'), 'myh_test/sensi.txt')

def add(strr):
    data=''
    for i in range(len(strr)):
        data+='*'
    return data
    
data = open(path, 'rb').read().decode('utf-8').split('\r\n')
for i in data:
    if type_in.find(i)!=-1:
        type_in= type_in.replace(i, add(i))

print(type_in)

