# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
list_vowel = ["а","е","ё","и","о","у","ю","я","ю"]


def is_there_a_rithm(list_need:list)->list: #проверям есть ли ритм
    count=0
    a = list_need[0]
    for i in range(len(list_need)):
        if list_need[i] == a:
            count+=1
        else:
            count+=0
    if len(list_need) == count:
        print("Парам пам-пам")
    else:
        print("Парам-пам")
    

def find_count_of_vowel(str_need:str)->str: #считаем количество гласных в слове
    list_need = list(str_need)
    count = 0
    for i in range(len(list_need)):
        if list_need[i] in list_vowel:
            count+=1
        else:
            count+=0
    return count


phrase= input("Винни, введи свой стих для проверки: ")
list_word = phrase.split()
# print(list_word)
list_result = (list(map(find_count_of_vowel, list_word)))
# print(list_result)
print(is_there_a_rithm(list_result))

