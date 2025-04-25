def generate_matrix(key):
    matrix = []
    used = set()
    key = key.upper().replace('J','I')
    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)
    
    for i in range(ord('A'), ord('Z')):
        ch = chr(i)
        if ch not in used and ch != 'J':
            matrix.append(ch)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col
    return None

def prepare_text(text):
    text = text.upper().replace('J','I')
    prepared = ""
    i = 0
    while i < len(text):
        ch1 = text[i]
        ch2 = text[i+1] if (i + 1 < len(text)) else 'X'
        if ch1 == ch2:
            prepared += ch1 + 'X'
            i+=1
        else:
            prepared+=ch1+ch2
            i+=2
    if len(prepared) % 2 != 0:
        prepared+='X'
    return prepared

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        ch1, ch2 = text[i], text[i+1]
        r1, c1 = find_position(matrix, ch1)
        r2, c2 = find_position(matrix, ch2)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

def playfair_decrypt(text, key):
    matrix = generate_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        ch1, ch2 = text[i], text[i+1]
        r1, c1 = find_position(matrix, ch1)
        r2, c2 = find_position(matrix, ch2)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

plaintext = input("Enter plaintext: ")
key = input("Enter keyword: ")

encrypted = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(encrypted, key)

print(f"\nEncrypted Text: {encrypted}")
print(f"Decrypted Text: {decrypted}")