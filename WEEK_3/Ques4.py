import math

def ORDER_OF_R(r, n):
    if math.gcd(r,n) != 1:
        return None
    k = 1
    power = r % n
    while power != 1:
        power = (power * r) % n
        k += 1
        if k > n:
            return None
    return k

r = int(input('Enter r : '))
n = int(input('Enetr n : '))
order = ORDER_OF_R(r, n)
if order:
    print(f'Order of {r} under modulo {n} is {order}')
else:
    print(f'Order Does not exist for {r} under modulo {n}')