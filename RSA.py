from math import gcd

p = int(input("Enter Prime p: "))
q = int(input("Enter Prime q: "))
m = int(input(f"Enter message (number<{p*q}): "))

n = p*q
phi = (p-1)*(q-1)

for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

d = pow(e, -1, phi)
c = pow(m, e, n)
m2 = pow(c, d, n)

print("Public Key:", e, n)
print("Private Key:", d, n)
print("Encrypted:", c)
print("Decrypted:", m2)
