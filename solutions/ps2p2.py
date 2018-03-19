# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card company each month.

balance = 3926
annualInterestRate = 0.2


def bal_end_year(bal, pay):
    un_pay_bal = previous_bal = bal
    for i in range(0, 12):
        un_pay_bal = previous_bal - pay
        previous_bal = un_pay_bal + un_pay_bal * mon_rate
    return un_pay_bal


pay_mont = 10
mon_rate = annualInterestRate / 12.0
while bal_end_year(balance, pay_mont) > 0:
    pay_mont += 10
print("Lowest Payment:", pay_mont)
