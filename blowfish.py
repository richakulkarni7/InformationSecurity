from Crypto.Cipher import Blowfish
bs = Blowfish.block_size
import os
encryptedpass = "myverystrongpassword"
plaintextMessage = "TejaTeju"
iv = os.urandom(Blowfish.block_size)
bs = Blowfish.block_size
cipher = Blowfish.new(encryptedpass, Blowfish.MODE_CBC, iv)
ct = iv + cipher.encrypt(plaintextMessage)
print(ct)
cipher = Blowfish.new(encryptedpass, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ct[bs:])
print (msg)