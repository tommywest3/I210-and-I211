#Weekly Challenge 1
#Thomas West III
#thopwest

#Problem 1
lst = eval(input("Please enter a list: "))
middle = int((len(lst) / 2))
print("The middle element is", lst[middle])

#Problem 2
lst2 = eval(input("Please enter a list of words: "))
for word in lst2:
    if word != "secret":
        print(word)
