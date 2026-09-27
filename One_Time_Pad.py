import random
import string

m = input("Message: ").upper()
k = ''.join(random.choice(string.ascii_uppercase) for _ in m)

e = ''.join(chr((ord(a)+ord(b)-130) % 26+65) for a, b in zip(m, k))
d = ''.join(chr((ord(a)-ord(b)) % 26+65) for a, b in zip(e, k))

print("Key:", k)
print("Encrypted:", e)
print("Decrypted:", d)
