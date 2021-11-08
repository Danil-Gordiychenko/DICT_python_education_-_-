def CreditCalculator():
    principal = int(input('Enter the loan principal:\n'))
    print("What do you want to calculate?")
    print("type 'm' – for number of monthly payments,")
    print("type 'p' – for the monthly payment:")
    x = input()
    if x == 'm':
        n = int(input('Enter the monthly payment:\n'))
        y = principal / n
        z = round(y)
        print('It will take', z, 'months to repay the loan')
    elif x == 'p':
        months = int(input('Enter the number of months:\n'))
        payment = principal / months
        if principal % months == 0:
            payment = principal // months
            print('Your monthly payment =', payment)
        elif payment != int:
            z = round(payment)
            last_payment = principal - ((months - 1) * payment)
            y = round(last_payment)
            print('Your monthly payment =', z, 'and the last payment =', y)

CreditCalculator()
