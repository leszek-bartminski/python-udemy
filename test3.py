import random

test = ['a', 'b', 'c']

length = [0, 1, 2]

# for i in range(len(test)):    #1sza iteracja: i = 0, k = 1
#     k = random.randint(0, len(length) - 1) # k = 1
#     testtablica = []
#     if test[k] not in testtablica:
#         testtablica[i].append(test[k])
#             # test = [a, b, c] / test = [a, a] ||  
#     length.pop(k) # length = [1, 2]
# print(testtablica)

already_used = []
password = []
# for i in range(len(test)):    #1sza iteracja: i = 0, k = 1 # 2ga iteracja: i = 1, k = 0
#     k = random.randint(0, 2) # k = 0


#     if k not in already_used:
#         password.append(test[k]) # password = ['b']
#     else:
        
#     already_used.append(k) # already_used = [1]

already_used = []
password = []

while len(password) < 3:
    k = random.randint(0, 2) # k = 0


    if k not in already_used:
        password.append(test[k]) # password = ['b']

    already_used.append(k)

print(password)