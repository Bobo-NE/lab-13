#Задача 1
import math

girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", "Амелия", "Розамунда", "Янина", "Беатриса"]
a = girls[1:5]
print(a)
b = girls[3:8]
print(b)
c = girls[0:5]
c.remove("Кассандра")
print(c)
d = girls[2:6]
d.remove("Вирджиния")
print(d)
print() #Задача 2
L = [12, 3, 8, 125, 10, 98, 54, 199]
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])
print(L[5])
print(L[6])
print(L[7])
print()
n = math.log2(L[0])
n1 = math.log2(L[1])
n2 = math.log2(L[2])
n3 = math.log2(L[3])
n4 = math.log2(L[4])
n5 = math.log2(L[5])
n6 = math.log2(L[6])
n7 = math.log2(L[7])
print(n)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print()
L[5] = 0
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])
print(L[5])
print(L[6])
print(L[7])
print()
n = math.log2(L[0])
n1 = math.log2(L[1])
n2 = math.log2(L[2])
n3 = math.log2(L[3])
n4 = math.log2(L[4])
#n5 = math.log(L[5])
n6 = math.log2(L[6])
n7 = math.log2(L[7])
print(n)
print(n1)
print(n2)
print(n3)
print(n4)
#print(n5)
print(n6)
print(n7)
print()
#Задание4
numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]
print("Введите число от 1 до 10: ")
m = int(input())
m -= 1
print(numbers[m])
print()
#Задание3
age = [24, 35, 42, 27, 45, 48, 33]
for i in range(len(age)):
 V = age[i]**2
 print(V)






