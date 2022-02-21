str = 'X-DSPAM-Confidence:0.8475'
num1 = str.find(":")
num2 = str.find("5")
finalNum = str[num1 + 1: num2 + 1]
float(finalNum)
print(finalNum)
