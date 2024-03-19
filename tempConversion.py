
print('''
Avaialable Options
1 = Celsius to Farenheit
2 = Farenheit to Celsius''')
unit = input("Select your option: ")

if unit == '1':
    temp = int(input("Enter temperature in Celsius: "))
    temp_f = (temp * 9/5) + 32
    print("Temperature in Farenheit is", temp_f)

elif unit == '2':
    temp = int(input("Enter temperature in Farenheit: "))
    temp_c = (temp - 32) * 5/9
    print("Temperature in Celsius is", temp_c)
    
else:
    print("Invalid Choice")