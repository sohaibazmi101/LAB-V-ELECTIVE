def caesar_encrypt(text, shift):
    encrypted = " "
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = input('Enter text to encrypt : ')
shift = int(input("Enter shft value : "))
enc = caesar_encrypt(text, shift)
dec = caesar_decrypt(enc, shift)
print(f"Original : {text}")
print(f"Encrypted : {enc}")
print(f"Decrypted : {dec}")