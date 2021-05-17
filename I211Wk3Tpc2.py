#Practiceing findall
#Thomas West

#Import the re module
import re

#Create the word list into a variable and display them
string = "Original: test loon etta panet aaw meek ziiim try"
print(string)

#Make a way to match words with two or more vowels in a row for the string above
print("Match:", re.findall('[a-z]*[aeiou][aeiou]+\w', string))
