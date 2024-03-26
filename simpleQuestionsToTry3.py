# Author - Viruna Cooray
# Date 26th March 2024
# Endless loop and safely exit it with a break statement

count = 0

while True:
    count += 5
    
    if count >= 51:
        break
    
    print(count)

#----------------------------------------------------------

while True:
    user_input = input("Enter 'exit' to quit: ").lower()
    
    if user_input == 'exit':
        break