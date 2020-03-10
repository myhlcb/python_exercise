#  使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os
path=os.path.join(os.path.abspath('.'),'myh_test')
IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
Imgae_Font = 'arial.ttf'
text = ''.join(random.sample(string.ascii_lowercase + string.digits, 4))
def colorRandom():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
im = Image.new(IMAGE_MODE, (300, 100), IMAGE_BG_COLOR)
draw = ImageDraw.Draw(im)
for w in range(300):
    for h in range(100):
        # 绘制描点
        if 2 < random.randint(1, 100): 
            draw.point((w,h),fill=colorRandom())
        
font = ImageFont.truetype(path +'/'+ Imgae_Font, 60)
font_width, font_height = font.getsize(text)
print(font_width, font_height)
x = (300 - font_width) / 2
y = (100 - font_height) / 2
for i in text:
    draw.text((x, y), i,  fill=colorRandom(),font=font)
    x += font_width / 4
    y += font_height / 4
# 模糊
im = im.filter(ImageFilter.BLUR)
im.save('secret.jpg','JPEG')
im.show()    