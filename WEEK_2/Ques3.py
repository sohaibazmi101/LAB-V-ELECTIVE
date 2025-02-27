def GCD(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
if GCD(num1, num2) == 1:
    print(f'{num1} and {num2} are Coprime')
else:
    print(f'{num1} and {num2} are NOT Coprime')