# a = 2
# match a:
#     case 1:
#         print('Единица')
#     case 2:
#         print('Двойка')
#     case 3:
#         print('Тройка')
#     case _: # Во всех остальных случаях
#         print('Не единица, не двойка и не тройка')

#________________

# Task 2. 
# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

# trigger = True
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             if not(x or y or z) != (not x) and (not y) and (not z):
#                 print("Верно")
#                 trigger = False
#                 break
# if trigger: print("Всегда верно")

#__________________________

# a = pow(3, 3)  - возведение в степень (3 в третьей степени)

#_____________

# a = 4
# b = a
# a += 5
# print(b) 

#_____________

# from array import array


# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)

# c = a.copy()
# # c = a[:] - копия при помощи среза

# a.append(5)
# c.append(7)

# print(a)
# print(c)

#__________________

# Напишите пограмму принимающую на вход число N и выдает последовательность из 
# N-членов
# N= 5 -> 1, -3, 9, -27, 81

# def posled(N):
#     array = []
#     num = 1
#     for i in range(0, N):
#         #array.append(num) 
#         array.append((-3)** i)
#         #num *= -3
#     return array

# array = posled(5)
# print(array)

# ____________________

# list = []
# list.append(3)
# dict = {}
# dict[1] = 'Vova'
# dict[89] = 'Igor'
# dict[1] = 'Valya'

# print(list)
# print(dict)
# print(dict.get(3))

# _____________________


# Для натурального n создать индекс-значение,
# состоящий из элементов последовательности 3n + 1
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# from array import array


# dict = {}
# N = 6
# for i in range(1, N + 1):
#     dict[i] = 3 * i + 1
# print(dict)

# def newArray(d):
#     array = []
#     for i in range(d):
#         x = int(input(f"Введите {i + 1} элемент "))
#         array.append(x)
#     return array

# array = newArray(5)
# print(array)
# ____________________________________

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определит количество вхождений одной строки в другую

# text1 = str(input("Введите 1-ю строку: "))
# text2 = str(input("Введите 2-ю строку: "))

# count = 0

# for i in range(len(text2) + 1):
#     dlina = len(text1) + i
#     if text1 == text2[i : dlina]:
#         count += 1

# print(count)

#_________________________________

# Решение этой же задачи методом count:

# textFirst = input('Введите первый текст: ')
# textSecond = input('Введите второй текст: ')

# string = ' '
# substring = ' '

# if len(textFirst) > len(textSecond):
#     string = textFirst
#     substring = textSecond
# else:
#     string = textSecond
#     substring = textFirst

# print(string.count(substring))

# ____________________________

# Решение этой же задачи путем проверки элементов:
# как только появляется первое совпадение, включется еще один внутренний 
# цикл проверки последующих элементов:

textFirst = input('Введите первый текст: ')
textSecond = input('Введите второй текст: ')
string = ' '
subString = ' '
count = 0
counter = 0

for i in range(len(string) - len(subString) + 1):
    if string[i] == subString[0]:
        counterIn = 0
        for k in range(len(subString)):
            if subString[0 + k] == string[i + k]:
                counterIn += 1
        if counterIn == len(subString):
            counter += 1

print(f'Counter = {counter}')
