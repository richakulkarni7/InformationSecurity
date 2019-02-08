import random
def gcd(a, b):
	while True:
		temp = a%b
		if temp==0:
			return b
		a = b
		b = temp

print("Enter two prime numbers: " )
p, q = input().split()
p = int(p)
q = int(q)
n = p*q
phi = (p-1)*(q-1)

#getting the public key
e = random.choice(range(2, phi))
while gcd(e, phi)!=1:
	e = random.choice(range(2, phi))
print("Public key: ("+str(e)+", "+str(n)+")")	

#getting the private key
k = 0
while True:
	temp = (k*phi + 1)
	if(temp%e==0):
		d = int(temp/e)
		break
	k+=1	
print("Private key: ("+str(d)+", "+str(n)+")")

#converting plaintext input to numerical form and encrypting
cipher_input = list(input("Enter text to be encrypted: "))
ciphered = []
for x in range(0, len(cipher_input)):
	cipher_input[x] = ord(cipher_input[x])-96
	ciphered.append(cipher_input[x]**e%n)

#converting encrypted numerical to encrypted text
ciphered_text = ""
for x in ciphered:
	ciphered_text += chr(x+96)
print("Encrypted text: "+''.join(map(str, ciphered_text)))

#decrypting encrypted numerical and converting to text
deciphered = []
for x in ciphered:
	deciphered.append(chr((x**d%n)+96))
cipher_output = "".join(deciphered)
print("Decrypted text: "+cipher_output)
