
def count(str, letter):
    num = 0
    for position in str:
        if position == letter:
            num = num + 1
    return(num)





str = input("Enter a string:")
letter = input("Enter a letter")
print(count(str, letter))
