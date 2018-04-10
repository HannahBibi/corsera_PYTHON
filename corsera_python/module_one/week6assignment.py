def normal_pay(h, r):
    if h > 40:
        return 40 * r
    else:
        return h * r


def overtime_hrs(h):
    if h > 40:
        return h - 40
    else:
        return 0


def overtime_pay(h, r):
    return overtime_hrs(h) * (r * 1.5)


def computepay(h, r):
    return overtime_pay(h, r) + normal_pay(h,r)
