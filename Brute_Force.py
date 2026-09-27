m = input("Message: ").upper()
k = int(input("Key: "))

e = ''.join(chr((ord(c)-65+k) % 26+65) if c.isalpha() else c for c in m)
print("Encrypted:", e)

print("\nBrute Force:")
for i in range(26):
    d = ''.join(chr((ord(c)-65-i) % 26+65) if c.isalpha() else c for c in e)
    print(i, d)
