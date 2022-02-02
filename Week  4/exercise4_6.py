def computepay(h, r):
    if h > 40:
        standardPay = r * 40
        overtimePay = (h - 40) * (r * 1.5)
        total = standardPay + overtimePay
        return (total)

    else:
        pay = h * r
        return (pay)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))


print("Pay ", computepay(hrs, rate))
