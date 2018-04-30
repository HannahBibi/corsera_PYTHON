def normal_pay(hours_worked, rate_of_pay):
    if hours_worked > 40:
        return 40 * rate_of_pay
    else:
        total = hours_worked * rate_of_pay
    return total


def overtime_pay(normal_hours_pay, overtime_hours, hours_worked, rate_of_pay, overtime_extra):
    overtime_hrs = overtime_hours - hours_worked
    overtime_rate = rate_of_pay * overtime_extra
    total_overtime_pay = overtime_hrs * overtime_rate
    total = total_overtime_pay + normal_hours_pay
    return total


