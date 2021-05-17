#Manipulating data from files
#Thomas West

#Import the re module
import re

#Open the file with read capabilites
filename = open("message.txt", "r")

#Turn the read file into text
content = filename.read()
#Change all emails to "redacted"
content = re.sub("[a-z]+[0-9]*[@][a-z]+[.][a-z]+", "redacted", content)
#Change all phone numbers to "redacted"
content = re.sub("[(]*[0-9]{3}[)]*[\s][0-9]{3}[-][0-9]{4}", "redacted", content)
#Change all proper names to "redacted"
content = re.sub("[A-Z][a-z]+[\s][A-Z][a-z]+", "redacted", content)

#Close the file
filename.close()

#Create the copy with write capabilities
copy = open("messageRedacted.txt", "w")
#Write the "redacted" messages onto the copy
copy.write(content)
#Close the copy file
copy.close()

#Print the messages from the assignment
print("Reading in from: message.txt")
print("Redacted file saved as: messageRedacted.txt")

