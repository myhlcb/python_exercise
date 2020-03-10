# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os
import re
import glob
path = os.path.join(os.path.abspath('.'), 'myh_test')

for i in glob.glob(path+"/1.js"):
    # print(len(open(i).readlines()))
    name=os.path.basename(i)
    length = len(open(i).readlines())
    code=re.compile('//')
    codelength = len(code.findall(str(open(i).readlines())))
    
    bank = open(i).readlines().count('\n')
    print("在文件%s中代码共有%s行，其中注释%s行，空行%s行"%(name,length,codelength,bank))