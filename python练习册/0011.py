# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
import os
type_in = input("input:")
judge_flag=False
path = os.path.join(os.path.abspath('.'), 'myh_test/sensi.txt')

data = open(path, 'rb').read().decode('utf-8').split('\r\n')
for i in data:
    if type_in.find(i)!=-1:
        judge_flag=True

if judge_flag:
    print('freedam')
else:
    print('human rights')