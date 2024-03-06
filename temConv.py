
print('''
Avaialable units
f = Farenheit
c = Celsius''')
unit = input("Select your unit: ")

if unit.lower() == 'f':
    temp = int(input("Enter temperature in Farenheit: "))
    temp_c = (temp - 32) * 5/9
    print("Temperature in Celsius is", temp_c)
    
elif unit.lower() == 'c':
    temp = int(input("Enter temperature in Celsius: "))
    temp_f = temp * 5/9 +32
    print("Temperature in Farenheit is", temp_f)
    
else:
    print("Error")
