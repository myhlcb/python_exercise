# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
import pymysql

import os
import random,string
mydb = pymysql.connect(
    host= 'localhost',
    user='root',
    passwd='123456',
    # auth_plugin='mysql_native_password',
    database='myh_runoob'
)
cursor = mydb.cursor()
# sqlStr = "CREATE TABLE `bills` (\
#   `id` int NOT NULL AUTO_INCREMENT,\
#   `coupon` varchar(20) NOT NULL,\
#   PRIMARY KEY (`id`)\
# ) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4; "
# cursor.execute(sqlStr)
def getCoupons():
  list=[]
  for i in range(200):
        coupon = ''.join(random.sample(string.ascii_letters + string.digits, 12))
        list.append(coupon)
  return list
list = getCoupons()
sql = 'insert into `bills`(`coupon`)values (%s)'
# print(tuple(list))
try:
  cursor.executemany(sql, tuple(list))
  print('success')
  mydb.commit()
except NameError as identifier:
  print('error',identifier)
finally:
  print('end')