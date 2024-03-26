
age = int(input("Enter your age: "))
print('''
Available membership options:
    Basic
    Premium
    None''')
member = input("Enter membership status: ").lower()

if member == 'basic' or member == 'premium' or member == 'none':
    if age <= 16:
        print("You are not eligible due to age.")
    
    elif age > 17 and age < 26:
        if member == 'premium':
            print("You are eligible for a special discount!")
        else:
            print("You are not eligible for any discounts.")
    
    elif age > 60:
        print("You are eligible for a senior discount!")
    
    else:
        print("You are not eligible for any discounts.")
else:
    print('Invalid membership status. Please enter Basic, Premium, or None')

