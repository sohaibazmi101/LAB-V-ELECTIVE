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

def FIND_NARCISSISTIC(num):
    start = 10 ** (num-1) if num > 1 else 0
    end = 10 ** num
    narcissistic_numbers = [num for num in range(start, end) if IS_ARMSTRONG(num)]
    if narcissistic_numbers:
        print(f" All {num}-DIGIT NARCISSISTIC number : {narcissistic_numbers}")
    else:
        print(f"No {num}-Digit narcissistic numbers found")

num = int(input('Enter digt : '))
FIND_NARCISSISTIC(num)