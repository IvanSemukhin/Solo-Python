# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(0, 12):
    min_pay = balance * monthlyPaymentRate
    un_pay = balance - min_pay
    interest = annualInterestRate/12.0*un_pay
    balance = interest + un_pay
print("Remaining balance:", round(balance, 2))
