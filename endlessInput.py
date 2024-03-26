# Author - Viruna Cooray
# Date 26th March 2024
# Create an endless while loop that takes user inputs until the user types "exit"

count = None

while True:
    user_input = input("Enter 'exit' to quit: ").lower()
    
    if user_input == 'exit':
        break