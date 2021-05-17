#Weekly Challenge 4
#Thomas West III

#Import the re and urllib.request module
import re, urllib.request

#Ask the user for the movie plot wikilink
user_movie = input("Please enter a movie link: ")
#Convert the user input to a real website
user_website = "https://en.m.wikipedia.org/wiki/" + user_movie

#Open the web page 
website = urllib.request.urlopen(user_website)
#Read the content 
contents = website.read().decode(errors = "replace")

#Ask the user for a name to be replaced
character_name = input("Please enter a character to replace: ")

#Ask the user for a name to take the place of the real name
replaced_name = input("Please enter a person to replace them with: ")

#Find the section with just the plot in it
plot_wiki = re.findall('(?<=id="Plot">Plot</span>).+?(?=<span class="mw-headline")', contents, re.DOTALL)[0]
changeable_wiki = str(re.findall('(?<=<p>).+?(?=\n</p>)', plot_wiki))

#Replace the original name with the new name given by the user
replaced_wiki = re.sub(character_name, replaced_name, changeable_wiki)

print(replaced_wiki)

#Close the web page
website.close()
