from string import printable
import random
key = ''.join(random.sample(printable, len(printable)))
 
def encode(plaintext, key):
    return ''.join(key[printable.index(char)] for char in plaintext)
 
def decode(plaintext, key):
    return ''.join(printable[key.index(char)] for char in plaintext)
 
original = "A simple example."
encoded = encode(original, key)
decoded = decode(encoded, key)
print("The original is:", original)
print("Encrypting it with the key:", key)
print("Gives:", encoded)
print("Decoding it by the same key gives:", decoded)