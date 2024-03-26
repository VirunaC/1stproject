# Author - Viruna Cooray
# Date 26th March 2024
# Skip even numbers using the continue statement

count = 0

while count < 25:
    count += 1
    if count % 2 == 0:
        continue
    print(count)