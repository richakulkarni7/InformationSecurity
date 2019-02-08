from sympy.crypto.crypto import encipher_hill, decipher_hill
from sympy import Matrix
pt = "ACT"
key = Matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
ct = encipher_hill(pt, key)
print("Ciphered: ", ct)
print("Deciphered:", decipher_hill(ct, key))