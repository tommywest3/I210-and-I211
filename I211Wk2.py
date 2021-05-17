#Practicing with Dictionaries

total = 0
while True:
    new_num = input("Please enter a number or STOP: ")
    if new_num.upper() == "STOP":
        print("The total sum is", total)
        break
    else:
        total += int(new_num)

nums = []
for i in range(10):
    new_num = input("Please enter a number: ")
    nums.append(new_num)
    even = []
    odd = []
    non_whole = []
    for i in range(len(nums)):
        nums[i] = float(nums[i])
        if nums[i] % 2 == 0:
            even.append(nums[i])
        elif nums[i] % 2 != 0 and (nums[i] + 1) % 2 != 0:
            non_whole.append(nums[i])
        elif nums[i] % 2 != 0:
            odd.append(nums[i])
print(even, odd, non_whole)

scores = {"Dave":125, "Abby":100, "Carrie":275, "Ben":150}

print("Current Players: ")
for key in scores.keys():
    print(key, end = " ")
print()
player_name = input("Please enter a Player Name: ")

if player_name in scores.keys():
    print("The score for", player_name, "is", scores.get(player_name), ".")
else:
    print("The score for", player_name, "is not found.")
