#Реализуйте алгоритм перемешивания списка.

import random 
listRandom = [] 
num = int(input('Ведите количество элементов в списке: '))
for i in range(num):
    num2=int(input('Ведите элемент в список: '))
    listRandom.append(num2)
print(listRandom)
random.shuffle(listRandom) 
print(listRandom)

