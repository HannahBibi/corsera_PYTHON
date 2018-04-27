hours_worked = input('Enter hours of work:')
rate_of_pay = input('Enter rate of pay:')
h = float(hours_worked)
r = float(rate_of_pay)
if hours_worked > 40:
    regular_pay = h * r
    overtime_pay = (h - 40) * (r * 1.5)
    total_pay = r + overtime_pay
else:
    total_pay = h * r
print('Pay:', total_pay)
