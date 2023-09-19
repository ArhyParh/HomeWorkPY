# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

def print_operatiom_table(operation,num_rows,num_columns):
    for i in range(num_columns):
        for j in range(num_rows):
            list_i=[operation((j+1),(i+1)) for j in range(num_columns)]
        print(list_i)    
          
    
            

x_need = int(input("Введите желаемое число строк: "))
y_need = int(input("Введите желаемое число столбцов: "))
print_operatiom_table(lambda x,y:x*y, x_need,y_need) #в возвращенном значения лямбда можно указать :(x*y,x/y,x+y,x-y)