
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print('''
Select an operator from below
+ is Addition
- is Subtraction
* is Multiplication
/ is Division''')

op = input("What's your operator? ")

if op == '+':
    print(num1 + num2)
    
elif op == '-':
    print(num1 - num2)
    
elif op == '*':
    print(num1 * num2)
    
elif op == '/':
    print(num1 / num2)

else:
    print("You're an idiot, follow the instructions.")