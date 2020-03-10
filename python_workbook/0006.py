#  你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
import os
import glob
import re
path = os.path.join(os.path.abspath('.'), 'myh_test')
# print(path)
# print(os.walk(path))
# # os.walk(path)
# for root, dirs, files in os.walk(path):
#     print(root, dirs, files, 111)

for file in glob.glob(path+'/*.txt'):
    keyword=re.compile('no')
    # print(len(keyword.findall(str(open(file).readlines()))))
    length=len(keyword.findall(str(open(file).readlines())))
    # print(os.path.basename(file))
    name=os.path.basename(file)
    print('在%s文件中 %s为关键字,共出现了%s次'%(name,'no',length))