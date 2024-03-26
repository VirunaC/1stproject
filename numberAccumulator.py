# Author - Viruna Cooray
# Date 26th March 2024
# Use a while loop to accumulate the sum of
# user-entered numbers until the user enters 0

sum = 0

while True:
    num = int(input("Enter a number(Enter 0 to quit): "))
    if num == 0:
        print(f'The sum before quitting was {sum}')
        break
    sum += num
    print(f'The sum is {sum}')