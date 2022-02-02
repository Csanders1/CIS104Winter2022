def computegrade(score):
    if score > 1.0:
        return("ERROR: Out of Range")

    elif score < 0.0:
        return("ERROR Out of Range")

    elif score >= 0.9:
        return("A")

    elif score >= 0.8:
        return("B")

    elif score >= 0.7:
        return("C")

    elif score >= 0.6:
        return("D")

    elif score <= 0.6:
        return("F")




try:
    score = float(input("Enter Score"))

except:
    print("Bad Input")
    exit()

print("Your grade is: ", computegrade(score))
