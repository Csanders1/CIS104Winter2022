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
    letters = words[1].split("@")
    letter = letters[1]

    nameDict[letter] = nameDict.get(letter, 0) + 1


print(nameDict)
