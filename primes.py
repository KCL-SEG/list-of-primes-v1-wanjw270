"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    count = 0
    while count < number_of_primes:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            list.append(num)
        num += 1   
        count += 1 
    return list
