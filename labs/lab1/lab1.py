"""
Dylan Benton Embrey
1/19/2022
Computer Programming Labs 1: Interest Rate
This is my work.
"""
def monthly_interest():


    # show the input of the net credit card statement balance
    annual_interest_rate = eval(input('current annual interest rate:'))
    billing_cycle_time = eval(input('number of days in current billing cycle:'))
    net_credit_card_balance = eval(input('show previous net credit card balance amount:'))
    cycle_payment_amount = eval(input('the payment amount made on the cycle day:'))
    day_payment = eval(input('day of cycle payment was made:'))
    # within function:step1 multiply the previous net balance with the number of days on the billing cycle using "*"
    step1 = net_credit_card_balance * billing_cycle_time
    # display result to the user
    print(step1)
    # within function:step2 multiply the payment by the subtraction function using "*(-)"
    step2 = cycle_payment_amount * (billing_cycle_time-day_payment)
    # display result to the user
    print(step2)
    # within function:step3 minus the amount made in step2 by the amount made from step1 using "-"
    step3 = step1 - step2
    # display result to the user
    print(step3)
    # within function:average_daily_balance divide the result in step3 by the input:billing_cycle_time
    average_daily_balance = step3/billing_cycle_time
    # display result to the user
    print(average_daily_balance)
    # within function:monthly_interest_rate divide annual interest rate by 12 and then divide by 100 using "/12/100"
    monthly_interest_rate = annual_interest_rate/12/100
    # display result to the user
    print(monthly_interest_rate)
    # within function:monthly_interest_charge multiply the monthly_interest_rate by the average_daily_balance using "*"
    monthly_interest_charge = monthly_interest_rate * average_daily_balance
    print(monthly_interest_charge)
    # display result to the user
monthly_interest()
