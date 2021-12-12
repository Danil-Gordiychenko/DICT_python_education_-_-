import math
import argparse


parser = argparse.ArgumentParser(description="Credit Calculator Project")
parser.add_argument('--type')
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()


if args.type == "diff" and args.principal > 0 and args.periods > 0 and args.interest > 0:
    i = args.interest / (12 * 100)
    m = 1
    D = 0
    while m <= args.periods:
        d = (args.principal / args.periods) + (i * (args.principal - (args.principal * (m - 1) / args.periods)))
        print("Month {}: paid out {}".format(m, math.ceil(d)))
        m += 1
        D += math.ceil(d)
    print("Overpayment = {}".format(D - args.principal))

elif args.type == "annuity" and args.principal is not None and args.payment is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    x = args.payment / (args.payment - (i * args.principal))
    degree = math.log(x, (1 + i))
    ceil = math.ceil(degree)
    year = ceil / 12
    round_up = str(round(year, (1)))
    y = list(round_up)
    print("It will take", y[0], "years and", y[2], "months to repay this loan!")
    print(f'Overpayment = {args.payment * ceil - args.principal}')

elif args.type == 'annuity' and args.periods is not None and args.payment is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    num = pow(1 + i, args.periods)
    d = (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)
    x = round(args.payment / d)
    result_p = math.floor(float(args.payment / ((i * num) / (num - 1))))
    print("Your loan principal =", x, "!")
    print(f'Overpayment = {args.payment * args.periods - result_p}')

elif args.type == 'annuity' and args.periods is not None and args.principal is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    value = (i * math.pow(1 + i, args.periods)) / (
                math.pow(1 + i, args.periods) - 1)
    monthly_payment = args.principal * value
    overpayment = abs(args.periods * math.ceil(monthly_payment) - args.principal)
    monthly_payment = math.ceil(monthly_payment)
    print(f'Your annuity payment = {monthly_payment}!')
    print(f'Overpayment = {overpayment}')