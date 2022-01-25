hrs = float(input("Enter Hours: "))
rate = float(input("Enter pay rate: "))
if hrs > 40:
    standardPay = rate * 40
    overtimePay = (hrs - 40) * (rate * 1.5)
    overtimeTotal = overtimePay + standardPay
    print (overtimeTotal)
elif hrs <= 40:
    grossPay = hrs * rate
    print (grossPay)
