alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(choice, text, shift):
    
    repeat = "y"
    incorrect_choice = True

    while incorrect_choice == True:
        choice = input("Choose function. Press 1 for encrypt or press 2 for decrypt. Any other key is not accepted:\n")
        if choice == "1" or choice == "2":
            incorrect_choice = False
            if choice == "1":
                choice = "1"
            else:
                choice = "2"
        else:
            incorrect_choice = True

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    lista = list(text)
    output = ""

    for i in range(len(text)):
        if choice == "1":
            lista[i] = (alphabet[((alphabet.index(text[i]) + shift) % 26)])
            print(lista)
        else:
            lista[i] = (alphabet[26 -(26 - ((alphabet.index(text[i]) - shift) % 26))])
            print(lista)
    output = "".join(lista)
    print(output)



    while repeat == "y":
        repeat = input("If you want to continue, 'y'. If not, press 'n' or any other key to terminate program:\n").lower()
        print(repeat)
        if repeat == "y":
            # text = input("Type your message:\n").lower()
            # shift = int(input("Type the shift number:\n"))        
            ceasar(choice, text, shift)
        else:
            break
        break

choice = 0
text = ""
shift = 0

ceasar(choice, text, shift) 