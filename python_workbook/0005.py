#  你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
import glob
from PIL import Image

path = os.path.join(os.path.abspath('.'), 'myh_test')

arr = glob.glob(path + '/*.jpg')

for i in arr:
    print(i)
    im = Image.open(i)
    im.thumbnail((1136, 640))
    print(im.format,im.size,im.mode)
    im.save(i,'JPEG')
