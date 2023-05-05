#   Homework 3:
# Задача 1: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих cтроках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример: n = 5; элементы 1 2 3 4 5; x = 3; 

# Задача 2: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


 #Задача 3: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


# Decision
# Task 1:

# n = int(input('Введите размер элементов списка: '))
# list_n = input('Введите элементы списка через пробел: ').split()
# arr = list(map(int, list_n))
# x = int (input('Введите число х: '))
# count = 0
# for i in range(n):
#     if arr[i] == x:
#         count += 1
# print(f'Число {x} встречается в списке А {count} раз.')



# # Task 2: 
# n = abs(int(input('Введите количество элементов массива А: ')))
# Ai = input("Введите целые числа: ").split()
# A= list(map(int, Ai))
# if len(A) != n or n == 0:
#     print('Введенные элементы не соответствуют заявленному количеству')
# else:
    
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     min = abs(X - A[0])
#     index = 0
#     for i in range(1, n):
#         count = abs(X - A[i])
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')


   
# # Task 3:
list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

word = input("Введите слово: ").upper()
summ = 0
for i in word:
    for k, v in list_letters.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")
