#Add links from website to a list
#Thomas West

#Import the re and url lib request module
import re, urllib.request

#Define the function
def wikilinks(url):
    #Open the Wkipedia link when called
    website = urllib.request.urlopen(url)
    #Read the content 
    contents = website.read().decode(errors = "replace")
    #Create a way to add the links to a list
    links = re.findall('[/][wiki]+[/][A-Z][a-z]+\w[:]*[A-Z]*[a-z]+\w', contents)
    #Close the webpage
    website.close()
    #Return the list
    return links


