import string

key = input("Key: ").upper().replace('J', 'I')
m = input("Message: ").upper().replace('J', 'I').replace(' ', '')
a = ''.join(dict.fromkeys(key+string.ascii_uppercase.replace('J', '')))
g = [a[i:i+5] for i in range(0, 25, 5)]

p = ''
i = 0
while i < len(m):
    x = m[i]
    y = m[i+1] if i+1 < len(m) and m[i+1] != x else 'X'
    p += x+y
    i += 1 if y == 'X' else 2


def play(s, d):
    r = ''
    for x, y in zip(s[::2], s[1::2]):
        a, b = next((i, j) for i in range(5) for j in range(5) if g[i][j] == x)
        c, e = next((i, j) for i in range(5) for j in range(5) if g[i][j] == y)
        if a == c:
            r += g[a][(b+d) % 5]+g[c][(e+d) % 5]
        elif b == e:
            r += g[(a+d) % 5][b]+g[(c+d) % 5][e]
        else:
            r += g[a][e]+g[c][b]
    return r


e = play(p, 1)
print("Encrypted:", e)
print("Decrypted:", play(e, -1))
