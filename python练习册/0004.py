# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
import os
pattern = re.compile('no')
path = os.path.join(os.path.abspath('.'), 'myh_test/coupon.txt',)
print(len(pattern.findall(re.sub(r'\\n','',str(open(path).readlines())))))

# print(re.sub(r'\\n','',str(open(path).readlines())))