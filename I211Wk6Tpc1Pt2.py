#Jumping to different links from wikipedia site
#Thomas West

#Import the re, urllib request, and random module
import re, urllib.request, random

#Ask the user for the Wikipedia article
user_wiki = input("Where would you like to start? ")
#Ask the user how many times they would like to jump
user_number = eval(input("How many jumps? "))

#Open the url 
website = urllib.request.urlopen(user_wiki)
#Read the content 
contents = website.read().decode(errors = "replace")

#Find the links in the website
links = re.findall('[/][wiki]+[/][A-Z][a-z]+\w[:]*[A-Z]*[a-z]+\w', contents)

#Loop through how many times the user wants to jump
for i in range(user_number):
    print("Jumping from:", random.choice(links))
    print("To:", random.choice(links))
    
    
