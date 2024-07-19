from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}


sign_list = []
for key in operations:
    sign_list += key

sign_list = "\n".join(sign_list)

# print(sign_list)


def calculation(a):
    global result
    sign = input("Choose operation sign:\n" + sign_list + "\n") 
    b = float(input("Give second number:\n")) #b=3
    result = operations[sign](a, b) #sign=*, result = 15    
    print(f"{a} {sign} {b} = {result}")
    
def calculator(a):
    i = 0
    a = float(input("Give first number:\n")) #a=5 
    choice = 'y'
    while choice == 'y':
        
        i += 1
        if i > 1:
            # print(result)
            # a = result # 15
            calculation(a)
            # print(a)
        else:
            calculation(a)
        
        a = result
        # sign = input("Choose operation sign:\n" + sign_list + "\n") 
        # b = int(input("Give second number:\n"))
        # result = operations[sign](a, b)     
        # print(result)
        choice = input("Type 'y' to continue or type 'n' to start a new calculation or any other key to exit program:\n").lower()
    if choice == 'n':
        calculator(a) 
# a = int(input("Give first number:\n"))
# sign = input("Choose operation sign:\n" + sign_list + "\n") 
# b = int(input("Give second number:\n"))
sign = ' '
a = 0

print(logo)
calculator(a)
# print(sign)
# print(operations[sign])