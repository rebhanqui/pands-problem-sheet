#SCRIPT TO COUNT HOW MANY E'S IN A TXT FILE
#Author: Rebecca Quinn

#permanent file path
FILENAME = "/Users/rebeccaquinn/Desktop/pands-problem-sheet/countfile.txt"

#opens file and reads it with 'r'
file = open(FILENAME, 'r')

#puts file content to string
data = file.read()

#requests user to select a letter
letter = input("Pick a letter to see how many occurences are in the count file: ")

#count counts how many times the chosen letter occurs
occurences = data.count(letter)

#prints result
print(f"There are {occurences} letter {letter}'s in the count file")

