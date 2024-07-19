#print("Hello " + input("What's your name?\n"))

# city = print("Hello!\n" + input("Where did you grow up?"))
# pet = print(input("What's your favourite pet?\n"))

# print("Your band name can be: " + city + pet)

# print("Hello"[4])

# "Hello"[4]

# print(123 + 123)

# Można używać podkreślenia, żeby rozdzielać cyfry w zapisie dużych liczb
print(type(print(12_3 + 1_2_3)))

a = str(print(12_3 + 1_2_3))

print(type(a))

c = "123"

b = int(str(c))
print(type(b))



# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# a = int(two_digit_number[0])
# b = int(two_digit_number[1])

# print(str(a) + "+" + str(b) + " = " + str(a + b))


# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# height = float(height)
# weight = float(weight)

# bmi = weight / (height ** 2)

# bmi = int(bmi)

# print(bmi)




# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# years_left = 90 - int(age)
# days = years_left * 365
# weeks = years_left * 52
# months = years_left * 12


# print(f"You have {days} days, {weeks} weeks, and {months} months left.")



#TIP CALCULATOR - project day 2
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill *= (1 + tip/100)

bill /= people

print(round(bill, 3))



# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")



# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height**2)


if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")





#Leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 != 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


#Pizza order

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "L":
    bill = 25
elif size == "M":
    bill = 20
else:
    bill = 15

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")