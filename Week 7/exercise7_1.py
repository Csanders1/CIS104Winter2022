fname = input("Enter a file name:")

freal = open(fname)

for line in freal:
    lines = line.rstrip()
    output = lines.upper()
    print(output)
