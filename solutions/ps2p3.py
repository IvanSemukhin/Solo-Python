balance = 999999
annualInterestRate = 0.18
mon_rate = annualInterestRate / 12.0


def bal_end_year(bal, pay):
    un_pay_bal = previous_bal = bal
    for i in range(0, 12):
        un_pay_bal = previous_bal - pay
        previous_bal = un_pay_bal + un_pay_bal * mon_rate
    return un_pay_bal


def acc_pay(bal):
    lo = bal / 12
    hi = (bal * (1 + mon_rate) ** 12) / 12.0
    while True:
        pay = (lo + hi) / 2
        answer = bal_end_year(bal, pay)
        if 0.0 == round(answer, 2):
            return pay
        elif bal_end_year(bal, pay) < 0.0:
            hi = pay
        else:
            lo = pay


print("Lowest Payment:", round(acc_pay(balance), 2))
