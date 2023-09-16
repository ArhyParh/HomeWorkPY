from random import randint
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def generate_random_list(size:int, lover:int, upper:int)->int:
    list_back =[]
    for i in range(size):
        list_back.append(randint(lover,upper))
    return list_back


def find_result_between(list_back, min, max):
    print([x for x in list_back if min < x and x < max])

list_i = generate_random_list(10,-10,10)
print(list_i)
find_result_between(list_i,0,10)