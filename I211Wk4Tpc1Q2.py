#Practicing findall
#Thomas West

#Import the re module
import re

#Open the file with read capabilities
filename = open("quote.txt", "r")
#Turn the read file into text
content = filename.read()

#Print out the words beginning with a capital letter
print(re.findall("[A-Z][a-z]+", content))
#Print out the words ending in "ing"
print(re.findall("[\w]+[i]+[n]+[g]+", content))
#Print out the words with two "a"s in them
print(re.findall("[\w]*[a][\w]*[a][\w]+", content))
#Print out all the phrases that begin and end with a comma
print(content.split(","))
#Print out the number of words that begin with the letter "v"
print(re.findall("[v][\w]+", content))
