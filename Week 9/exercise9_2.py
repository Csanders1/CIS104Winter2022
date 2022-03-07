name = input("Enter file:")
nameDict = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()

    nameDict[words[2]] = nameDict.get(words[2], 0) + 1


print(nameDict)
