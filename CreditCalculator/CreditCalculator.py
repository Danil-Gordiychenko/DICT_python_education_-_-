import math
import sys
try:
    args = sys.argv
    type = args[1]
    if type == "--type=diff":
        p = args[2]
        if p[:12] == "--principal=":
            p = int(p[12:])
            n = args[3]
            if n[:10] == "--periods=":
                n = int(n[10:])
                i_percent = args[4]
                if i_percent[:11] == "--interest=":
                    i_percent = float(i_percent[11:])
                    i = i_percent / (12 * 100)
                    m = 1
                    D = 0
                    while m <= n:
                        d = (p/n) + (i*(p - (p*(m-1)/n)))
                        print("Month {}: paid out {}".format(m, math.ceil(d)))
                        m += 1
                        D += math.ceil(d)
                    print("Overpayment = {}".format(D - p))
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    elif type == '--type=annuity':
        p = args[2]
        if p[:12] == '--principal=':
            p = int(p[12:])
            a = args[3]
            if a[:10] == '--payment=':
                a = int(a[10:])
                interest = args[4]
                if interest[:11] == '--interest=':
                    interest = float(interest[11:])
                    i = interest / 1200
                    x = a / (a - (i * p))
                    degree = math.log(x, (1 + i))
                    o = math.ceil(degree)
                    year = o / 12
                    round_up = round(year, (1))
                    r = str(round_up)
                    y = list(r)
                    print("It will take", y[0], "years and", y[2], "months to repay this loan!")
                    print("Overpayment =", a * o -p)
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        elif p[:10] == '--payment=':
            p = float(p[10:])
            n = args[3]
            if n[:10] == '--periods=':
                n = int(n[10:])
                interest = args[4]
                if interest[:11] == '--interest=':
                    interest = float(interest[11:])
                    i = interest / 1200
                    num = pow(1 + i, n)
                    b = i * (1 + i) ** n
                    c = (1 + i) ** n - 1
                    d = b / c
                    x = p / d
                    z = round(x)
                    result_p = math.floor(float(p / ((i * num) / (num - 1))))
                    print("Your loan principal =", z, "!")
                    print('Overpayment =', p * n - result_p)
                else:
                    print("Incorrect Parameters")
            else:
                print("Incorrect Parameters")
        else:
            print("Incorrect Parameters")
    else:
        print("Incorrect Parameters")

except Exception:
    print("Incorrect Parameters")