import string
import random

m = input("Message: ").upper()
k = ''.join(random.sample(string.ascii_uppercase, 26))

e = m.translate(str.maketrans(string.ascii_uppercase, k))
d = e.translate(str.maketrans(k, string.ascii_uppercase))

print("Key:", k)
print("Encrypted:", e)
print("Decrypted:", d)
