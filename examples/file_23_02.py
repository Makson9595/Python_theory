# a mod b
# 15 mod 5 = 2
# 17 integer 5 = 3
# 5 + 5 + 5

# 14 mod 4 = 2
# 14 integer 4 = 3

# 128 min
# 1 час = 60

# часы = 128 integer 60 = 2
# минуты = 128 mod 60 = 8

# 5759 mod 10
# 5759 integer 10

# 0-9

# ------------------- Арифметические операторы

"""
2 + 3
Out[2]: 5

10 / 2
Out[3]: 5.0

5 * 5 * 5 * 5
Out[4]: 625

5 ** 4
Out[5]: 625

(-5) ** 4
Out[6]: 625

(-3) * (-3) * (-3) * (-3)
Out[7]: 81

(-4) * (-4) * (-4)
Out[8]: -64

(-2) * (-2) * (-2)
Out[9]: -8

17 / 5
Out[10]: 3.4

17 // 5
Out[11]: 3

17 % 5
Out[12]: 2

-17 // 5
Out[13]: -4

-7
Out[14]: -7

-11
Out[15]: -11
"""

# ------------------- Функция print()

print(1, 8, 7, 34)
# 4 -  значений <=> аргументов

print("Hello", "World")
# 2 -  значений <=> аргументов

print("Hello, World")
#  1 - значение <=> аргумент

print("Alice", 18, True, None, 2 + 3)
print("Alice", 18, True, None, "2 + 3")
print("Alice", 18, True, None, 2, "+", 3)

print()

# ------------------- Параметры sep и end

print("Alice", 18, True, None, 2 + 3, sep="|")
print("Alice", 18, True, None, "2 + 3", sep="|")
print("Alice", 18, True, None, 2, "+", 3, sep="|", end="\t")
print("Alice", 18, True, None, 2, "+", 3, sep="|", end="\n")

# separator - разделитель
# end - конец

# -------------------Управляющие символы

print("Привет, мир\rPython")
print("Hello wor\bl\bd\b")

print("hello \new world")
print("It\"s me!")
print("hello \\new world")
