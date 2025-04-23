import time
def brute_force_attack(password, length):
    max = length ** 10
    atempt = 0
    start_time = time.time()
    while atempt < max:
        guess = str(atempt).zfill(length)
        if guess == password:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Password Cracked : Password = {guess}")
            print(f"Total Time taken : {time_taken:.4f}")
            print(f"Totsl attempts : {atempt + 1}")
            return
        atempt+=1
    print("Failded to crack the passwird")

length = int(input("Enter length of password : "))
pwd = input("Enter password : ")
brute_force_attack(pwd, length)