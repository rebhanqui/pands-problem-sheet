#SCRIPT TO COUNT HOW MANY E'S IN A TXT FILE
#Author: Rebecca Quinn

#permanent file path
FILENAME = "/Users/rebeccaquinn/Desktop/pands-problem-sheet/countfile.txt"

#opens file and reads it with 'r'
file = open(FILENAME, 'r')

#puts file content to string
data = file.read()

#letter to count
letter = ("e")

#letter in bother cases
letterlower = ("e")
letterupper = ("E")

#count counts how many times the chosen letter occurs in both upper and lowercase
loweroccurences = data.count(letterlower)
upperoccurences = data.count(letterupper)

#combination of occurances of letter cases
occurences = int(loweroccurences + upperoccurences)

#prints result
print(f"There are {occurences} letter {letter}'s in the count file")