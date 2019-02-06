from string import printable
import random
print(printable)
key = ''.join(random.sample(printable, len(printable)))
 
def encode(plaintext, key):
    return ''.join(key[printable.index(char)] for char in plaintext)
 
def decode(plaintext, key):
    return ''.join(printable[key.index(char)] for char in plaintext)
 
original = "A simple example."
encoded = encode(original, key)
decoded = decode(encoded, key)
print("""The original is: {}
Encoding it with the key: {}
Gives: {}
Decoding it by the same key gives: {}""".format(
    original, key, encoded, decoded))