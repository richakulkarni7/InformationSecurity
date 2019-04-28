import hashlib
str= "hello"
result = hashlib.md5(str.encode()) 
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
print("The byte equivalent of hash is : ", end ="")
print(result.digest())