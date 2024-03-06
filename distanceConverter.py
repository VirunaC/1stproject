
principal = int(input("What's the principal amount: "))
roi = int(input("What is the rate of interest: "))
time = int(input("Enter the duration in months: "))

interest = (principal * roi / 100)
totalInterest = (interest * time)

print("Your interest per month is Rs.", interest, "and your total interest for the period is Rs.", totalInterest)