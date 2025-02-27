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

def IS_MERSENNE(num):
    if IS_PRIME(num):
        if ((num + 1) & num) == 0:
            return True
    return False

num = int(input('Enter a number : '))
print(f'{num} is MERSENNE ? {IS_MERSENNE(num)}')