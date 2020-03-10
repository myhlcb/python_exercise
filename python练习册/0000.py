# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont,ImageFilter,ImageDraw
import os
path = os.path.join(os.path.abspath('.'), '4disland', '0000', 'myWife.jpg')
im = Image.open(path)
print(im.format)
# rgb2xyz = (0.412453,0.357580, 0.180423, 0,
#            0.212671,0.715160, 0.072169, 0,
#            0.019334, 0.119193, 0.950227, 0)
# new_im=im.convert('L',rgb2xyz)
# new_im.show()
print(im.info)
region = im.crop((0, 0, 210, 610))
im.paste(region, (100, 100 ))
bluF = im.filter(ImageFilter.BLUR)
conf = im.filter(ImageFilter.CONTOUR)
edgeF = im.filter(ImageFilter.FIND_EDGES)
# im.show()
# bluF.show()
# conf.show()
# edgeF.show()

draw = ImageDraw.Draw(im)
draw.text((100, 100), 'myWife', 'red',Wordsize=60)
im.show()