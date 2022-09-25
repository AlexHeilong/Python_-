# print('Hello world')
# 1. Напишите программу, которая принимает на вход два числа и 
# проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# print(' ')
# print('Введите а')
# a = int(input())

# print('Введите а')
# b = int(input())
# print(' ')
# print(a, b )
# print(' ')

# if a**2 == b or b**2 == a:
#     print(True)
# else:
#     print(False)




# list = [45, 68, 35, 2, 77, 25]
# max = 0
# for i in list:
#     if i > max:
#         max = i

# print(max)

# def array(m):
#     x = []
#     for i in range(m):
#         a = int(input(f'Введите x{i + 1}: '))
#         x.append(a)
    
#     return x

# def max_el(array):
    
#     maxim = 0

#     for i in range(len(array)):
#         if array[i] > array[maxim]:
#             maxim = i

#     return array[maxim]

# l = int(input('Введите количество элементов: '))
# new_array = array(l)
# maxim = max_el(new_array)
# print(f'Максимальный элемент: {maxim}')


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# num = int(input('Введите число: '))
# list = []
# for i in range(- num, num + 1):
#     list.append(i)
# print(list)

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = float(input('Введите число: '))
# if (num *10) % 10 != 0:
#     print(int(num * 10) % 10)
# else:
#     print('нет')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Введите число: '))
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 30:
    print('Yes')
else:
    print('No')
    
# @STONECF
