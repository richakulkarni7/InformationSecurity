#for this to work, go to the pyDH module's folder in the Python directory's lib/site-packages, and find __init__.py.
#in __init__.py chnage the line to: from .pyDH import DiffieHellman

import pyDH
d1 = pyDH.DiffieHellman()
d2 = pyDH.DiffieHellman()
d1_pubkey = d1.gen_public_key()
d2_pubkey = d2.gen_public_key()
print(d1_pubkey)
print(d2_pubkey)
d1_sharedkey = d1.gen_shared_key(d2_pubkey)
d2_sharedkey = d2.gen_shared_key(d1_pubkey)
print(d1_sharedkey == d2_sharedkey)
print(d1_sharedkey)