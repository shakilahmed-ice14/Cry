def t(m, k):
    n = len(k)
    return ''.join(m[i::n] for i in sorted(range(n), key=lambda i: k[i]))


m = input("Message: ").replace(' ', '')
k1 = input("Key 1: ")
k2 = input("Key 2: ")

print("Encrypted:", t(t(m, k1), k2))
