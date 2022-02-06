#2
#Написать скрипт, который выводит на экран «True», если элементы программно задаваемого списка представляют собой возрастающую
#последовательность, иначе – «False».
from random import randint
x = randint(1,15)
a = [randint(1,10) for i in range(x)]
print(a)
print(False not in (a[i] < a[i+1] for i in range(len(a)-1)))