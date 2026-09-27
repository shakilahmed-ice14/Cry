m = input("Message: ")
k = int(input("Key: "))

e = ''.join(chr((ord(c)-65+k) % 26+65) if c.isupper()
            else chr((ord(c)-97+k) % 26+97) if c.isalpha() else c for c in m)
d = ''.join(chr((ord(c)-65-k) % 26+65) if c.isupper()
            else chr((ord(c)-97-k) % 26+97) if c.isalpha() else c for c in e)

print("Encrypted:", e)
print("Decrypted:", d)
