# Author - Viruna Cooray
# Date 26th March 2024
# Generate a multiplication table for a number provided by the user up to 10

num = int(input("Enter number: "))

for count in range(1,11):
    num_mult = num*count
    print(num, "x", count, "=", num_mult) 
    