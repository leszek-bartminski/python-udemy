import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# print(len((letters)))

# all = letters + numbers + symbols

# print(len(all))

# del(all[:52])
# print(all)

letter_component = []

symbol_component = []

number_component = []

for i in range(0, nr_letters):                
    letter_component.append(letters[random.randint(0, len(letters))])

for i in range(0, nr_symbols):                
    symbol_component.append(symbols[random.randint(0, len(symbols))])

for i in range(0, nr_numbers):                
    number_component.append(numbers[random.randint(0, len(numbers))])

password = []

password = letter_component + symbol_component + number_component

print(password)

random_pass = []

for i in range(0, len(password)):
    n = random.randint(0, len(password))
    random_pass.append(password[n])
    password.remove(random_pass[i])

print(random_pass)
    