hours = input("Enter Hours: ")
rate = input("Enter pay rate: ")
try:
    hrs = float(hours)
    rte = float(rate)
except:
    print("ERROR Please Enter Numeric Input")
    quit()

if hrs > 40:
    standardPay = rte * 40
    overtimePay = (hrs - 40) * (rte * 1.5)
    overtimeTotal = overtimePay + standardPay
    print (overtimeTotal)
elif hrs <= 40:
    grossPay = hrs * rte
    print (grossPay)
