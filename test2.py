import random

test = ['a', 'b', 'c']

length = [0, 1, 2]

for i in range(len(test)):    #1sza iteracja: i = 0, k = 1
    k = random.randint(0, len(length) - 1) # k = 1
    testtablica = []
    if test[k] not in testtablica:
        testtablica[i].append(test[k])
            # test = [a, b, c] / test = [a, a] ||  
    length.pop(k) # length = [1, 2]
print(testtablica)



