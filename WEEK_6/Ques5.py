def xor(a, b):
    return ''.join(['0' if i == j else '1' for i, j in zip(a, b)])

def round_function(right, key):
    return xor(right, key)

def feistel_encrypt(plain_text, key, rounds=4):
    left = plain_text[:len(plain_text)//2]
    right = plain_text[len(plain_text)//2:]

    for i in range(rounds):
        temp = right
        right = xor(left, round_function(right, key))
        left = temp
        print(f"Round {i+1}: L = {left}, R = {right}")

    return left + right

def feistel_decrypt(cipher_text, key, rounds=4):
    left = cipher_text[:len(cipher_text)//2]
    right = cipher_text[len(cipher_text)//2:]

    for i in range(rounds):
        temp = left
        left = xor(right, round_function(left, key))
        right = temp
        print(f"Round {i+1}: L = {left}, R = {right}")

    return left + right

plain_text = "11001100"
key = "10101010"
print("Original:", plain_text)
cipher = feistel_encrypt(plain_text, key)
print("Encrypted:", cipher)

decrypted = feistel_decrypt(cipher, key)
print("Decrypted:", decrypted)