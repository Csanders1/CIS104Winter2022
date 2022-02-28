count = 0
fname = input("Enter file name: ")
try:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd")
        exit()
    fhand = open(fname)
except FileNotFoundError:
        print("File cannot be opened:", fname)
        exit()
for line in fhand:
    if line.startswith("Subject: "):
        count = count + 1

print("There were", count, "Subject lines in ", fname)
