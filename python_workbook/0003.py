# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import redis
import os
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

path = os.path.join(os.path.abspath('.'), 'myh_test/coupon.txt',)
file = open(path)
for i in file.readlines():
    # print(i[-13:-1],i[i.index('.')+1:i.rindex(' ')],i)
    key = "redis" + i[i.index('.') + 1:i.rindex(' ')]
    val=i[-13:-1]
    r.set(key,val)