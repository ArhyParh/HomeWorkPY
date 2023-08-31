# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random 

def fill_the_list(a): 
    while len(list)<a:
        list.append(int(random.randrange(0,2)))
    return list


def find_count(list):
    count = 0
    count2 = 0
    for i in range(len(list)):
        if list[i] > 0:
            count+=1
        else:
            count2+=1
    if count>count2:
        return count2
    else:
        return count


a = int(input("Ведите число монет, которые лежат на столе:"))
list = []
fill_the_list(a)

print(list)
print("Минимальное число монет, которые нужно перевернуть =",find_count(list))