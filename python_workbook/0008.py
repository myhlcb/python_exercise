# 一个HTML文件，找出里面的正文。
import os
import re
from bs4 import BeautifulSoup

path = os.path.join(os.path.abspath('.'), 'myh_test')
htmlDoc = open(path + '/test.html').read()
soup=BeautifulSoup(htmlDoc, "html.parser", from_encoding='utf-8')
body = soup.find('body')
print(body.get_text())