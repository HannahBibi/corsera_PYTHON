hrs_worked = input ("Enter hours:")
rate_of_pay = input ("Enter rate:")
h = float(hrs_worked)
r = float(rate_of_pay)

def overtime_hrs(h):
    return (h - 40)

def computepay(h,r):
    o = 0
    if(overtime_hrs(h) > 0):
        o = overtime_hrs(h) * (r * 1.5)
    n = 40 * r
    t = o + n
	return t

print (computepay(h,r))
