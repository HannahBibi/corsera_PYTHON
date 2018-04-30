def normal_pay(hours_worked, rate_of_pay):
    if hours_worked > 40:
        return 40 * rate_of_pay
    else:
        return hours_worked * rate_of_pay


def overtime_pay(normal_hrs, overtime_hrs, rate_of_pay):
    overtime_hrs = overtime_hrs - 40
    overtime_rate = rate_of_pay * 1.5
    total_overtime_pay = overtime_hrs * overtime_rate
    return total_overtime_pay + normal_hrs
