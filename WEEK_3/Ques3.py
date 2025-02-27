import math

def EULER_TOTIENTS(num):
    result = num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            while num % i == 0:
                num = num // i
            result *= (1 - (1/i))
    if num > 1:
        result *= (1 - (1/num))
    return int(result)

num = int(input('Enter a number : '))
print(f'Euler\'s Totient Function  of {num} is {EULER_TOTIENTS(num)}')