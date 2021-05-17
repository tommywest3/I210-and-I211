#Weekly Challenge 3
#Thomas West

#Import the re and urllib request module
import re, urllib.request

#Open the url 
website = urllib.request.urlopen("https://www.house.gov/representatives")
#Read the content 
contents = website.read().decode(errors = "replace")

#Find all the phone numbers in the website
nums = re.findall('[(]*[0-9]{3}[)]*\s[0-9]{3}-[0-9]{4}', contents)

#Print a total of all the numbers
print("Found the following", len(nums), "phone numbers")

#Loop through the contents of the webpage to find the phone numbers
for phone_numbers in nums:
    #Display all of the phone numbers found
    print(phone_numbers)


#Close the webpage after reading it
website.close()
