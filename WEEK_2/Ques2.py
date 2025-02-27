def GCD(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input("Enter  num1 : "))
num2 = int(input("Enter num2 : "))
print(GCD(num1, num2))