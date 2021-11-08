import math
def CreditCalculator():
    print("What do you want to calculate?")
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print("type 'p' – for the monthly payment:")
    x = input()
    if x == 'a':
        principal = int(input("Enter the loan principal:\n"))
        p = principal
        periods = int(input("Enter the number of periods:\n"))
        n = periods
        interest = int(input("Enter the loan interest:\n"))
        i = interest / 1200
        z = (i * ((1 + i) ** n))
        y = (1 + i) ** n
        a = (p * z) / (y - 1)
        d = math.ceil(a)
        print("Your monthly payment =", d, "!")
    elif x == 'n':
        principal = int(input("Enter the loan principal:\n"))
        p = principal
        payment = int(input("Enter the monthly payment:\n"))
        a = payment
        interest = int(input("Enter the loan interest:\n"))
        i = interest / 1200
        x = a/(a-(i*p))
        degree = math.log(x, (1+i))
        o = math.ceil(degree)
        year = o / 12
        round_up = round(year, (1))
        r = str(round_up)
        y = list(r)
        print("It will take", y[0], "years and", y[2], "months to repay this loan!")
    elif x == 'p':
        a = float(input("Enter the annuity payment:\n"))
        n = float(input("Enter the monthly payment:\n"))
        interest = float(input("Enter the loan interest:\n"))
        i = interest / 1200
        b = i*(1+i)**n
        c = (1+i)**n - 1
        d = b/c
        p = a/d
        z = round(p)
        print("Your monthly payment =", z, "!")
    else:
        print("Pleas try again")

CreditCalculator()
