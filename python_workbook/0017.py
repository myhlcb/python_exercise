# 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <students>
# <!-- 
# 	学生信息表
# 	"id" : [名字, 数学, 语文, 英文]
# -->
# {
# 	"1" : ["张三", 150, 120, 100],
# 	"2" : ["李四", 90, 99, 95],
# 	"3" : ["王五", 60, 66, 68]
# }
# </students>
# </root>

import xlrd
import json
from lxml import etree

def read_exl(file_name):
     exl = xlrd.open_workbook(file_name)
     exl_sheet = exl.sheet_by_name('student')
     print(exl,exl_sheet,222,exl_sheet.nrows)
     data = {}
     for i in range(exl_sheet.nrows):
         data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]
         
if __name__ == '__main__':
    content=read_exl('student.xls')