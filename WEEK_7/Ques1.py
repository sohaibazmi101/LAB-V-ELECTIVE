TABLE_SIZE = 10

def simple_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % TABLE_SIZE


def insert(table, key, value):
    index = simple_hash(key)
    if table[index] is None:
        table[index] = []
    table[index].append((key, value))
    print(f"Inserted ({key}, {value}) at index {index}")

def search(table, key):
    index = simple_hash(key)
    if table[index] is not None:
        for k, v in table[index]:
            if k == key:
                return v
    return None

def display_table(table):
    for i, item in enumerate(table):
        print(f"{i}: {item}")



hash_table = [None] * TABLE_SIZE

insert(hash_table, "Azmi", 99)
insert(hash_table, "Ghandhi", 88)
insert(hash_table, "Rahul", 77)
insert(hash_table, "Modi", 66)

print("\nHash Table:")
display_table(hash_table)

print("\nSearch for 'Modi':", search(hash_table, "Modi"))
print("Search for 'Yogi':", search(hash_table, "Yogi"))
print("Search for 'Rahul':", search(hash_table, "Rahul"))
