def normal_pay(hours_worked, rate_of_pay):
    if hours_worked < 0 or rate_of_pay < 0:
        return 0
    elif hours_worked > 40:
        return 40 * rate_of_pay
    else:
        return hours_worked * rate_of_pay


def overtime_pay(hours_worked, rate_of_pay):
    if hours_worked < 0 or rate_of_pay < 0:
        return 0
    elif hours_worked < 40:
        return 0
    else:
        overtime_hours = hours_worked - 40
        return overtime_hours * (rate_of_pay * 1.5)


def total_pay(hours_worked, rate_of_pay):
    return overtime_pay(hours_worked, rate_of_pay) + normal_pay(hours_worked, rate_of_pay)
