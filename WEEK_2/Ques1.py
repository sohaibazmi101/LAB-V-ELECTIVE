import math
def IS_PRIME(num):
    if(num <= 0):
        print('Number is not valid')
        return
    if(num == 1):
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if(num % i == 0):
            return False
        
    return True

number = int(input("ENter a number : "))
print(f"{number} is PRIME? {IS_PRIME(number)}")