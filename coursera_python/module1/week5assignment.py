hrs_worked = input("Enter Hours:")
rate_per_hour = input("Enter Rate:")
h = float(hrs_worked)
r = float(rate_per_hour)
if h > 40:
    regular_pay = h * r
    overtime_pay = (h - 40.0) * (r * 1.5)
    extra_pay = regular_pay + overtime_pay

else:
    extra_pay = h * r
print("Pay:", extra_pay)