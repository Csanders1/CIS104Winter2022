import string

count = 0
countsDict = dict()
rel_List = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:

            if letter not in countsDict:
                countsDict[letter] = 1
            else:
                countsDict[letter] += 1

for key, val in list(countsDict.items()):
    rel_List.append((val / count, key))

rel_List.sort(reverse=True)

for key, val in rel_List:
    print(key, val)
