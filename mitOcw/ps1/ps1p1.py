outstandingBalance = float(input("Enter the outstanding balance on your credit card: "))
interestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
monthlyPaymentRate = float(input("Enter the minimum payment rate as a decimal: "))

for month in range(1,13):
    monthlyInterestRate = interestRate/12
    minimumPaymentRate = monthlyPaymentRate * outstandingBalance
    interestPaid = monthlyInterestRate * outstandingBalance
    principalPaid = minimumPaymentRate - interestPaid
    outstandingBalance = outstandingBalance - principalPaid
    print("Month: ", round(month,2))
    print("Minimum monthly payment : $", round(minimumPaymentRate,2))
    print("Principal paid : $", round(principalPaid,2))
    print("Remaining balance: $", round(outstandingBalance,2))
    
