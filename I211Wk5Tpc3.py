#Asking the user for a webpage and outputting email addresses
#Thomas West

#Import the re and urllib request module
import re, urllib.request

#Ask the user for the web page
user_website = input("Search what page?")
#Open the url 
website = urllib.request.urlopen(user_website)
#Read the content 
contents = website.read().decode(errors = "replace")

#Find all the email addresses in the website
emails = re.findall('\w+@\w+.\w+', contents, re.DOTALL)

#Print a message saying that the program found email addresses
print("The email addresses in", user_website, "are:")

#Loop through the contents of the webpage to find the email addresses
for email_addresses in emails:
    #Display all of the email addresses found
    print(email_addresses)


#Close the webpage after reading it
website.close()
