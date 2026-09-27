from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

m = input("Enter message: ").encode()
k = input("Enter 8-character key: ").encode()

ci = DES.new(k, DES.MODE_ECB)

en = ci.encrypt(pad(m, DES.block_size))
de = unpad(ci.decrypt(en), DES.block_size)

print("Encrypted:", en.hex())
print("Decrypted:", de.decode())