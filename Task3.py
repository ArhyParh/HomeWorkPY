# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
def find_all_degree(n):
    i = 2
    list=[1]
    count = 1
    if n<=i:
        return -1
    while i< n:
        i=i*2
        if i<n:
            count+=1
        else:
            break
    return count

a = int(input("Введите число N: "))
print("Целые степени двойки, до числа N:")
for i in range(find_all_degree(a)):
    print (i+1)
