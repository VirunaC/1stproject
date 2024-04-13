# VC
# 09-04-2024
import math

def prime_number(num1):
    for i in range(2, int(math.sqrt(num1))):
        if num1 % i == 0:
            return False
    return True

prime = 101
if prime_number(prime):
    print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime number")