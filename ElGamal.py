p = int(input("p: "))
g = int(input("g: "))
x = int(input("Private key: "))
m = int(input("Message: "))

y = pow(g, x, p)
k = int(input("Random k: "))

a = pow(g, k, p)
b = m*pow(y, k, p) % p

print("Encrypted:", a, b)
print("Decrypted:", b*pow(pow(a, x, p), -1, p) % p)
