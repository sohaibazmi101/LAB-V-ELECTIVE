import numpy as np

def text_to_numers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join([chr(n % 26 + ord('A')) for n in numbers])

def pad_text(text):
    return text + 'X' if len(text) % 2 != 0 else text

def hill_encrypt(text, key_matrix):
    text = pad_text(text.upper().replace(" ",""))
    numbers = text_to_numers(text)
    encrypted = []
    for i in range(0, len(numbers), 2):
        a = numbers[i]
        b = numbers[i+1]

        c1 = (key_matrix[0][0] * a + key_matrix[0][1] * b)
        c2 = (key_matrix[1][0] * a + key_matrix[1][1] * b)
        encrypted.extend([c1, c2])
    return numbers_to_text(encrypted)

def mod_inverse(a,m):
    for x in range(1,m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under mod {m}")

def matrix_inverse_2x2(matrix, mod):
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % mod

    det_inv = mod_inverse(det, mod)

    inverse = [
        [(d * det_inv) % mod, (-b * det_inv) % mod],
        [(-c * det_inv) % mod, (a * det_inv) % mod]
    ]

    for i in range(2):
        for j in range(2):
            inverse[i][j] %= mod

    return inverse

def hill_decrypt(cipher_text, key_matrix):
    numbers = text_to_numers(cipher_text)
    decrypted = []

    inverse_key = matrix_inverse_2x2(key_matrix, 26)

    for i in range(0, len(numbers), 2):
        a = numbers[i]
        b = numbers[i+1]
        m1 = (inverse_key[0][0] * a + inverse_key[0][1] * b) % 26
        m2 = (inverse_key[1][0] * a + inverse_key[1][1] * b) % 26
        decrypted.extend([m1, m2])

    return numbers_to_text(decrypted)

key_matrix = [[3, 3], [2, 5]]

with open("input.txt", "r") as file:
    plain_text = file.read().strip().upper()

encrypted = hill_encrypt(plain_text, key_matrix)
with open("encrypted.txt", "w") as file:
    file.write(encrypted)

decrypted = hill_decrypt(encrypted, key_matrix)
with open("decrypted.txt", "w") as file:
    file.write(decrypted)

print("Encryption and Decryption complete.")
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)