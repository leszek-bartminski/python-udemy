import random

# # 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names_string = [i for i in names_string  if i != " " and i != ","]
# # names_string = names_string.split(",")
# # # 🚨 Don't change the code above 👆

# name = random.randint(0, len(names_string))

# print(names_string[name])

names_string = input("Give me everybody's names, separated by a comma. ")
names_string = names_string.replace(" ", "")
names = names_string.split(",")

print(names[random.randint(0, len(names) - 1)])

# name = random.randint(0, len(names) - 1)

# print(names[name] + " is going to buy the meal today!")