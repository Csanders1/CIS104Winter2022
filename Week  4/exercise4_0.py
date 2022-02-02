def maxFinder(num1, num2, num3):
    f = max(num1, num2, num3)
    return(f)


one = float(input("Enter a number"))
two = float(input("Enter a second number"))
three = float(input("Enter a third number"))

print("You chose: ", one, "," , two , "," , three)
print("The highest number was: ", maxFinder(one, two, three))
