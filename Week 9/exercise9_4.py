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
    nameDict[words[1]] = nameDict.get(words[1], 0) + 1

largest = None
largestName = None

for key in nameDict:

    if largest == None:
        largest = nameDict[key]

    if largest < nameDict[key]:
        largest = nameDict[key]
        largestName = key
print(largestName, largest)
