

def calculate_pay(hours_worked,rate_of_pay):
    if (float (rate_of_pay) < 0):
        return 0
    elif (float (hours_worked) < 0):
        return 0
    else:
        return float(hours_worked) * float(rate_of_pay)

