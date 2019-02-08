from pyDes import *

k = triple_des("\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", padmode=PAD_PKCS5)
data = input("Enter text to be encrypted: ").encode('ascii')
e = k.encrypt(data)
d = k.decrypt(e)
if d != data:
    print ("Error: decrypt does not match. %r != %r" % (data, e))
else:
    print ("Successful")
    print (d.decode('UTF-8'))