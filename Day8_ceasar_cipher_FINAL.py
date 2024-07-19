alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(choice, text, shift):


    lista = list(text)
    output = ""

    incorrect_choice = True


    while incorrect_choice == True:
        choice = input("Choose function. Press 1 for encrypt or press 2 for decrypt. Any other key is not accepted:")
        if choice == "1" or choice == "2":
            incorrect_choice = False
        else:
            incorrect_choice = True

    for i in range(len(text)):
        if choice == "1":
            lista[i] = (alphabet[((alphabet.index(text[i]) + shift) % 26)])
            print(lista)
        else:
            lista[i] = (alphabet[26 -(26 - ((alphabet.index(text[i]) - shift) % 26))])
            print(lista)
    output = "".join(lista)
    print(output)

ceasar(choice, text, shift)

repeat = "y"
while repeat == "y":
        while incorrect_choice == True:
        choice = input("Choose function. Press 1 for encrypt or press 2 for decrypt. Any other key is not accepted:")
        if choice == "1" or choice == "2":
            incorrect_choice = False
        else:
            incorrect_choice = True
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))        
        ceasar(text, shift, choice)
        
    choice = input("If you want to continue, 'y'. If not, press 'n' or any other key to terminate program.").lower()
    if choice == "y":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))        
        ceasar(text, shift, choice)
    else:
        break    


# def encrypt(text, shift):    
#     lista = list(text)
#     code = ""
#     for i in range(len(text)):
#         lista[i] = (alphabet[((alphabet.index(text[i]) + shift) % 26)])
#         print(lista)
#     code = "".join(lista)
#     print(code)

# def decrypt(coded_text, shift):
#     lista = list(coded_text)
#     text = ""
#     for i in range(len(coded_text)):
#         lista[i] = (alphabet[26 -(26 - ((alphabet.index(coded_text[i]) - shift) % 26))])
#         print(lista)
#     text = "".join(lista)
#     print(text)

# def flow():
#     incorrect_choice = True
    
#     while incorrect_choice == True:
#         choice = input("Choose function. Press 1 for encrypt or press 2 for decrypt. Any other key is not accepted:")
#         if choice == "1" or choice == "2":
#             incorrect_choice = False
#         else:
#             incorrect_choice = True

#     if choice == "1":
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         encrypt(text, shift)
#     else:
#         coded_text = input("Type encoded message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         decrypt(coded_text, shift)









     


        




