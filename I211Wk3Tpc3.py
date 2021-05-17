#Challenge: List Wikipedia Links
#Thomas West

#Import the re module
import re
#Import the url lib request module
import urllib.request

#Define the function
def wikilinks(url):
    #Open the url when called
    website = urllib.request.urlopen(url)
    #Read the content 
    contents = website.read().decode(errors = "replace")
    #Create a way to list all the Wikipedia links in the body of the page
    print(re.findall('[/][wiki]+[/][A-Z][a-z]+\w[:]*[A-Z]*[a-z]+\w', contents))
    #Close the webpage
    website.close()
