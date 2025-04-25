import random

def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

p = 23  
g = 5   

print("Publicly Shared:\n  Prime (p):", p, "\n  Base (g):", g)

a = random.randint(1, p-2)
A = power(g, a, p)

b = random.randint(1, p-2)
B = power(g, b, p) 

print("\nModi's Private Key (a):", a)
print("Yogi's Private Key (b):", b)

print("\nModi sends Public Key A:", A)
print("Yogi sends Public Key B:", B)

modi_shared_key = power(B, a, p) 
yogi_shared_key = power(A, b, p) 

print("\nShared Secret (Modi computes):", modi_shared_key)
print("Shared Secret (Yogi computes):", yogi_shared_key)

if modi_shared_key == yogi_shared_key:
    print("\nKey Exchange Successful! Shared key established securely.")
else:
    print("\nKey Mismatch!")
