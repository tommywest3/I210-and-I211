#Practicing writing to new files from webpage

#Import the url lib request module
import urllib.request

#Define the function with one argument
def getContent(url):
    #Open the url when called
    website = urllib.request.urlopen(url)
    #Read the content 
    contents = website.read().decode(errors = "replace")

    #Print the input call
    print("Attempting to access the page at this URL: ", url)
    #split the url so we can find the filename if there is one
    filename = url.split("/")[-1]

    #Check to see if the filename is named
    if ".html" not in filename:
        filename = "index.html"

    #Write to the new file
    file = open(filename, "w")
    file.write(contents)
    #Close the file after writing to it
    file.close()
    
    #Close the webpage after reading it
    website.close()

    #Print the results
    print("All done! Open", filename, "in your browser!")



    
