#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_characters = nr_letters + nr_numbers + nr_symbols



# for i in range(0, total_characters, int(total_characters / nr_letters)):
#     print(letters[random.randint(0, len(letters) - 1)])
#     for j in range(0, total_characters, int(total_characters / nr_numbers)):
#         print(numbers[random.randint(0, len(numbers) - 1)])
#         for k in range(0, total_characters, int(total_characters / nr_symbols)):
#             print(symbols[random.randint(0, len(symbols) - 1)])

password = []
all_characters = letters + symbols + numbers

if total_characters > 0:
    if nr_letters > 0 and nr_numbers > 0 and nr_symbols > 0:
        for i in range(0, total_characters):
            password.append(all_characters[random.randint(0, len(all_characters))])
            if password[i] in letters:
                nr_letters - 1
                all_characters = 
            elif password[i] in numbers:
                nr_numbers - 1
            elif password[i] in symbols:
                nr_symbols -1
            if nr_letters == 0:
                all_characters = symbols + numbers
            elif nr_symbols == 0:
                all_characters = letters + numbers                
            elif nr_numbers == 0:
                all_characters = symbols + letters
            elif nr_letters + nr_symbols == 0:
                all_characters = numbers
            elif nr_letters + nr_symbols + nr_numbers == 0:
                all_characters = []
print(password) 


already_used = []
password_randomised = []

while len(password_randomised) < len(password):
    k = random.randint(0, len(password) - 1) # k = 0


    if k not in already_used:
        password_randomised.append(password[k]) # password = ['b']

    already_used.append(k)

print(password_randomised)










