# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число: ')
sum = 0
for a in num:
    if a.isdigit():
        sum += int(a)

print(f"Сумма {num} равна: ", sum)