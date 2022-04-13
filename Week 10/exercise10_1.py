addressDict = dict()
lst = list()

fname = input("Enter file name: ")

try:
    fhand = open(fname)

except FileNotFoundError:

    print("File cannot be opened:", fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    else:
        if words[1] not in addressDict:
            addressDict[words[1]] = 1
        else:
            addressDict[words[1]] += 1

for key, val in list(addressDict.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(key, val)
