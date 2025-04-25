def xor_encrypt_decrypt(text, key):
    return ''.join([chr(ord(char) ^ key) for char in text])

text = 'Cyber Security'
keys = [0,1,5]
for key in keys:
    print(f'\nKey: {key}')
    encrypted = xor_encrypt_decrypt(text, key)
    print("Encypted: ",' '.join([f"{ord(c):02x}" for c in encrypted]))
    decrypted = xor_encrypt_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")