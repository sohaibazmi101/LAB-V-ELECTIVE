number = int(input('Enter a number : '))
sum = 0
for i in range(1, number//2 +1):
    if number % i == 0:
        sum += i

print(f"{number} is perfect? --> {sum == number}")