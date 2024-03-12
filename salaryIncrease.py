
old_salary = float(input("Enter current salary: "))
increase = float(input("Enter increase pecentage: "))

if old_salary > 0 and increase > 0 and increase <= 100:
    new_increase = old_salary * increase / 100
    new_salary = old_salary + new_increase
    print(f"Your new salary is Rs. {new_salary}")

else:
    print("Enter valid salary and valid percentage.")
