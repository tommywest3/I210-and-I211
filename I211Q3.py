#List names and print them on each new line after each space
#Thomas West

names = input("Please enter your name: ")
print("...")
names = names.split(' ')
for name in names:
    print(name, end = "\n")
    
    
