hoursDict = dict()
lst = list()

fname = input('Enter file name: ')

try:
    fhand = open(fname)

except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()

    if len(words) < 2 or words[0] != 'From':
        continue

    colFind = words[5].find(':')
    hour = words[5][:colFind]
    
    if hour not in hoursDict:
        hoursDict[hour] = 1
    else:
        hoursDict[hour] += 1

for key, val in list(hoursDict.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
