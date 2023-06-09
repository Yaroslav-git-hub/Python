# !Задача 2:
# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = input("Введите трехзначное число: ")
while len(num) != 3:
    print("\nВы ввели не трехзначное число!")
    num = input("Введите трехзначное число: ")

result = int(num[0]) + int(num[1]) + int(num[2])

print(f"{num} -> {result} ({num[0]} + {num[1]} + {num[2]})")


# !Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Сколько всего сделали журавликов: "))
x = s / 6
k = x * 4

# Таким способом они сделали по половинке журавликов, если число не кратно 6. На потом еще оставили :)
# Можно сделать проверку на кратность 6 , но я посчитал , что они всеже оставили половинки журавликов ))
# Если надо могу переделать
print(f"{s} -> {round(x,1)} {round(k,1)} {round(x,1)}")


# !Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


tiket = input("Введите номер билета: ")
while len(tiket) != 6:
    print("Увы такой билет не попадает под нашу лотерею :(")
    tiket = input("Введите номер билета: ")

luckyTiketFirst = int(tiket[0]) + int(tiket[1]) + int(tiket[2])
luckyTiketSecond = int(tiket[3]) + int(tiket[4]) + int(tiket[5])

if luckyTiketFirst == luckyTiketSecond:
    print(f"{tiket} -> yes")
else:
    print(f"{tiket} -> no")


# !Задача 8:
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки: "))
m = int(input("Введите размер шоколадки: "))

k = int(input("Сколько нужно отломить: "))
total = n * m

if k > total:
    print(f"{n} {m} {k} -> no")
elif k == total:
    print(f"{n} {m} {k} -> yes")
elif n == 1 or m == 1:
    if k % max(n, m) == 0:
        print(f"{n} {m} {k} -> yes")
    else:
        print(f"{n} {m} {k} -> no")
elif k % n == 0 or k % m == 0:
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")
