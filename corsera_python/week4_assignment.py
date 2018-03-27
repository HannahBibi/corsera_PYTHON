from corsera_python.hoursofpay import calculate_pay


hours_worked = input("Enter Hours:")
rate_of_pay = input("Enter Rate:")
total_pay = calculate_pay(hours_worked, rate_of_pay)
print ("Pay:", total_pay)
