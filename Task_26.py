# Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.

a = int(input("Введите число: "))
b = int(input("Введите степень: "))


def degree(a, b):
    if b == 1: return a
    return a * degree(a, b - 1)


print(degree(a, b))
