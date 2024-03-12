
marks = int(input("Enter marks: "))

    
if marks > 100:
    print("Wrong input")

elif marks >= 70:
    print(" You've received a 1st class")
    
elif marks >= 60:
    print(" You've received a 2nd upper")

elif marks >= 50:
    print(" You've received a 2nd lower")
    
elif marks >= 40:
    print(" You've received a basic degree")

elif marks < 0:
    print("Wrong input")

else:
    print("you've Failed")