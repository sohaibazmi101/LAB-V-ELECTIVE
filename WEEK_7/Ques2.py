from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def blowfish_encrypt(plain_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad(plain_text.encode(), Blowfish.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def blowfish_decrypt(cipher_text, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_padded = cipher.decrypt(cipher_text)
    decrypted = unpad(decrypted_padded, Blowfish.block_size)
    return decrypted.decode()

key = b'CONFEDENTIAL'
plain_text = input("Enter text : ")

print("Original Text:", plain_text)

encrypted = blowfish_encrypt(plain_text, key)
print("Encrypted:", encrypted.hex())

decrypted = blowfish_decrypt(encrypted, key)
print("Decrypted:", decrypted)
