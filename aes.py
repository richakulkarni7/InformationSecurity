# pip install pycryptodome
from Crypto.Cipher import AES
key = b'sixteen byte key'
plain = b'secret: 16 bytes'
cipher = AES.new(key, AES.MODE_EAX)
ciphertext = cipher.encrypt(plain)
print(ciphertext)
print(cipher.decrypt(ciphertext))
