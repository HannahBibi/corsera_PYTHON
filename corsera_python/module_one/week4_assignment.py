from corsera_python.module_one.hoursofpay import calculate_pay


hours_worked = input("Enter Hours:")
rate_of_pay = input("Enter Rate:")
total_pay = calculate_pay(hours_worked, rate_of_pay)
print ("Pay:", total_pay)
