# Author - Viruna Cooray
# Date 26th March 2024
# Utilize nested for loops to print a pyramid pattern of stars (*)

num = int(input("Enter number of levels: "))

for count in range(num):
    print("*" * (count+1))