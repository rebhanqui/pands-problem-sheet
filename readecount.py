FILENAME = readetext.txt

letter = str(input("Pick a letter: "))
print(letter)

def counte(FILENAME, letter):
    file = open(fileName, 'r')

    text = file.read()

    return text.count(letter)

#print(counte('readetext.txt', str(input("Pick a letter: "))))

counte('readetext.txt', letter)


def doAdd(num, letter):
    letterCount = {}
    letterCount[letter] = letterInput
    letterCount[num] = counte

    num, letter.append(letterCount)

print(letterCount)






