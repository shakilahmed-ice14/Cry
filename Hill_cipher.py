import numpy as np

K = np.array([[3, 3], [2, 5]])
m = input("Message: ").upper().replace(' ', '')
m += 'X'*(len(m) % 2)

e = ''
for i in range(0, len(m), 2):
    v = np.array([ord(c)-65 for c in m[i:i+2]])
    e += ''.join(chr(x % 26+65) for x in K@v)

D = pow(round(np.linalg.det(K)), -1, 26)*np.array([[5, -3], [-2, 3]]) % 26
d = ''
for i in range(0, len(e), 2):
    v = np.array([ord(c)-65 for c in e[i:i+2]])
    d += ''.join(chr(x % 26+65) for x in D@v)

print("Encrypted:", e)
print("Decrypted:", d)
