def IS_ARMSTRONG(num):
    num_str = str(num)
    sum = 0
    arm = num
    n_dig = len(num_str)
    while num != 0:
        rem = num % 10
        sum = sum + (rem ** n_dig)
        num = num // 10
    return arm == sum

number = int(input('Enter a number : '))
print(IS_ARMSTRONG(number))