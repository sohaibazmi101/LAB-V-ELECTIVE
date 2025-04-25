from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plain_text.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def aes_decrypt(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(cipher_text)
    return unpad(decrypted, AES.block_size).decode()

key = b'ThisIsA16ByteKey'
plain_text = input("Enter text : ")

print("Original Text:", plain_text)

encrypted = aes_encrypt(plain_text, key)
print("Encrypted (hex):", encrypted.hex())

decrypted = aes_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
