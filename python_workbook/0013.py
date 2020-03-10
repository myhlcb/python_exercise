# 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

import os
import urllib.request
from pyquery import PyQuery as pq
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
import requests

# def catch_tieba_pics(url):
    # content = urllib.request.urlopen(url)
    # method 1
    # bs = BeautifulSoup(content, 'html.parser')
    # allImg = bs.find_all('img',{"class":"card_head_img"})
    # print(allImg,33)
    # for i in allImg:
    #     download_pic(i['src'])

    # method2
    # print(content.read().decode('utf-8'),3333)
    # bs = pq(content.read())
    # for i in bs('img.card_head_img').items():
        # print(i,i.attr.src)
        # download_pic(i.attr['src'])

    # method3
    # bs=pq(url, method='get')
    # for i in bs('img.card_head_img').items():
    #     download_pic(i.attr['src'])

def catch_tieba_pics(url):
    r = requests.get(url).text
    bs = pq(r)
    for i in bs('img.card_head_img').items():
        print(i)
        download_pic(i.attr.src)




def download_pic(url):
    image_content = urllib.request.urlopen(url).read()
    print(urlsplit(url),11111)
    file_name = os.path.basename(urlsplit(url)[2])
    print(file_name,222)
    output = open(file_name, 'wb')
    output.write(image_content)
    output.close()


if __name__ == '__main__':
    catch_tieba_pics('http://tieba.baidu.com/p/2166231880')


# import os
# import urllib.request
# from bs4 import BeautifulSoup
# # from urlparse import urlsplit


# def catch_tieba_pics(url):
#     content = urllib.request.urlopen(url)
#     bs = BeautifulSoup(content, 'lxml')
#     print(bs.find_all('div'),1111)
#     for i in bs.find_all('img', {"class": "BDE_Image"}):
#         download_pic(i['src'])


# def download_pic(url):
#     image_content = urllib.urlopen(url).read()
#     # file_name = os.path.basename(urlsplit(url)[2])
#     # output = open(file_name, 'wb')
#     # output.write(image_content)
#     # output.close()


# if __name__ == '__main__':
#     catch_tieba_pics('http://tieba.baidu.com/p/2166231880')