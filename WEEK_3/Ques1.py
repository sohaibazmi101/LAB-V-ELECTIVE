def POWER_OF_TWO(num):
    if num <= 0:
        return False
    
    return (num & (num - 1)) == 0
num = int(input('Enter a number : '))
print(f'{num} IS POWER OF TWO? {POWER_OF_TWO(num)}')