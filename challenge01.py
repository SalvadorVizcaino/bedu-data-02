import random
number = int(input("Cuál es el tamaño de la lista? "))
counter = 1
list_random = []
while counter<=number:
    choice = random.randint(1, 2)
    index = random.randint(1, int(number))
    if choice == 1:
        value = int(counter * index)
    else:
        value = str(counter * index)
    list_random.append(value)
    counter = counter + 1
print(list_random)