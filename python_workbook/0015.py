#  纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
import os
import json
import xlwt

path = os.path.join(os.path.abspath('.'), 'myh_test/city.txt')
content = json.loads(open(path, 'rb').read().decode('utf-8'))


def save_into_excle(content, excle_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('student')
    l=['序号','姓名','语','数','外']
    row = 0
    col=0
    for i in range(len(l)):
        ws.write(row, col, l[i])
        col+=1
    row = 1
    col = 0
    print(content,content.items())
    print(sorted(content.items(),key=lambda x: x[0]))
    for k, v in sorted(content.items(), key=lambda d: d[0]):
        ws.write(row, col, k)
        # for i in v:
        col += 1
        ws.write(row, col, v)
        row += 1
        col=0
    wb.save(excle_name)    
save_into_excle(content,'222.xls')   