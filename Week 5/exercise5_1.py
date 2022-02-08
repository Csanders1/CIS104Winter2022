total = 0
count = 0
average = 0

while True:
    num = input("Enter a number ")

    if num == "done":
        break
    try:
        num = int(num)
    except:

        if num == "done":
            break

        print("Invalid Input")

        continue

    count = count + 1
    total = total + num

average = total/count
print("Total: ", total)
print("Count: ", count)
print("Average: ", average)
