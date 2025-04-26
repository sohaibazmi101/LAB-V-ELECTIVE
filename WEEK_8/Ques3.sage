p = 17
F = GF(p)
a = 2
b = 3

E = EllipticCurve(F, [a, b])
print("Elliptic Curve:", E)

P = E.gen(0)
print("Base Point P:", P)

private_key = 7
public_key = private_key * P

print("Private Key:", private_key)
print("Public Key:", public_key)

M = E([5, 1])
k = 3

C1 = k * P
C2 = M + k * public_key

print("Ciphertext C1:", C1)
print("Ciphertext C2:", C2)

decrypted_message = C2 - private_key * C1
print("Decrypted Message:", decrypted_message)
