'''
加密处理
'''

import hashlib

passwd = input('>>')

#加盐处理
salt = '*#06#'
hash = hashlib.md5(salt.encode()) #生成加密对象

hash.update(passwd.encode()) #加密处理

print(hash.hexdigest()) #获取加密码
