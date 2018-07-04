balance = int(input("Enter the outstanding balance on your credit card: "))
rate = float(input("Enter the annual credit card interest as a decimal: "))

monthlyPayment = 0
monthlyRate = rate/12
initialBalance = balance

while initialBalance > 0:
    monthlyPayment += 10
    initialBalance = balance
    months = 0

    while months < 12 and initialBalance > 0:
        months += 1
        interest = monthlyRate * initialBalance
        initialBalance -= monthlyPayment
        initialBalance += interest

print("RESULT")
print("Monthly payment to pay off debt in 1 year: " , monthlyPayment)
print("number of months needed: " , months)
print("Balance: " , initialBalance)
