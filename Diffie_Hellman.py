p, g = 23, 5
print(" Input Prime P : ", p)
a = int(input(f"Enter Alice's Private Key (1 to {p-2}): "))

b = int(input(f"Enter Bob's Private Key (1 to {p-2}): "))

A, B = pow(g, a, p), pow(g, b, p)
print("Alice's Public Key : ", A, "Bob's Public Key : ", B)

print("Alice's Secret Key : ", pow(B, a, p),
      "Bob's Secret Key : ", pow(A, b, p))
