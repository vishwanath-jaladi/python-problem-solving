# Program: Check Prime Number
# Description: Checks whether a given number is a prime number
# using a function.
def is_prime(number):
    if number < 2:
        return False
    is_divisible = False
    for i in range(2, number):
        if number % i == 0:
            is_divisible = True
    if is_divisible:
        return False
    else:
        return True
print(is_prime(11))
print(is_prime(9))
print(is_prime(2))
print(is_prime(1))




