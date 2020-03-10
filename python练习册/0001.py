# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import string
import random
import os
def getCoupon():
    data = ''
    for i in range(200):
        i=i+1
        data+='coupon no.'+str(i)+' '+''.join(random.sample(string.ascii_lowercase+string.digits,12))+'\n'
    return data
path = os.path.join(os.path.abspath('.'), 'myh_test', 'coupon.txt')
result=open(path, 'w')
result.write(getCoupon())
result.close()
