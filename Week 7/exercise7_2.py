fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count = count + 1
    pos1 = line.find(":")
    flt = float(line[pos1 + 1: ])
    total = total + flt


average = total/count
print("Average spam confidence:", average)
