import hashlib

message = input("Enter the message: ")

sha1_hash = hashlib.sha1(message.encode())

digest = sha1_hash.hexdigest()

print("\nSHA-1 Message Digest:")
print(digest)
