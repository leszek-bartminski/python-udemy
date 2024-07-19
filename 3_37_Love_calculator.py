name1 = input("Your name:\n")
name2 = input("The other name:\n")


combined_lowercase_names = (name1 + name2).lower()

total1 = 0

total1 += combined_lowercase_names.count('t')
total1 += combined_lowercase_names.count('r')
total1 += combined_lowercase_names.count('u')
total1 += combined_lowercase_names.count('e')

total2 = 0

total2 += combined_lowercase_names.count('l')
total2 += combined_lowercase_names.count('o')
total2 += combined_lowercase_names.count('v')
total2 += combined_lowercase_names.count('e')

score = total1*10 + total2

#print("Your score is " + str(total1) + str(total2) + ".")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")







