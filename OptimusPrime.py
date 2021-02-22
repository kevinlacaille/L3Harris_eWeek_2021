import numpy as np
from math import sqrt
from itertools import count, islice

def number_to_bits(n):
    return '{0:08b}'.format(n)
    
def number_of_ones(bits):
    return len(np.where(np.array([b == '1' for b in bits]))[0]) 

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

if __name__ == "__main__":
    
    LOWER = 100
    UPPER = 200

    number_of_primes = 0 

    for i in range(LOWER, UPPER + 1):
        bits = number_to_bits(i)
        num_ones = number_of_ones(bits)
        
        if is_prime(num_ones):
            number_of_primes += 1
        

    print(number_of_primes)