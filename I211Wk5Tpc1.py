#Finding parts of HTML using Python
#Thomas West

#Import the re and urllib request module
import re, urllib.request

#Open the url
website = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/test.html")
#Read the content
content = website.read().decode(errors = "replace")

#Find the head portion of html
head = re.findall('(?<=head>).+(?=/head>)', content, re.DOTALL)

#Find the body portion of html
body = re.findall('(?<=searchhere">).+(?=/body>)', content, re.DOTALL)

#Print out the web page that is being searched through 
print("Searching: http://cgi.soic.indiana.edu/~dpierz/test.html")

print("Head: > \n " , head)

print('Body: extras=""> \n ' , body)

#Close the webpage after reading it
website.close()
