import hashlib
def encrypt(s):
    m = hashlib.md5()
    m.update(bytes(s))
    return s.hexdigest()  #返回机密后的数据
