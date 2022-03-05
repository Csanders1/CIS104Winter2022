fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    sentence = line.split()
    if len(sentence) < 1 :
        continue
    if sentence[0] != ("From"):
        continue

    print(sentence[1])
    count = count + 1    

print("Total: ", count)
