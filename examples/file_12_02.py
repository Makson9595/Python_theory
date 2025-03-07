# Комментарии

2 + 2  # Здесь происходит операция сложение

# TODO: Ещё больше примеров о комментариях

# -----------------------------

# Литералы

# integer - целое
# float - вещественное/дробное
# string - строка

# False - Ложь
# True - Истина

# булевый тип
# False
# True

# None -  ничего *отсутствие значения

# null
name = None
name = "Ivan"

# -----------------------------

# 1000000 => 1 * 10 ^ 6
# 1E6
#
# 0.0001 => -1 * 10 ^ 4
# 1E-4

# -----------------------------
# Строки

# string_literal = "I want to become a professional programmer"
# another_string = 'Я хочу стать профессиональным программистом'

string_literal = "She said: \"Hello!\""
# string_literal = "She said: 'Hello!'"

another_string = 'It\'s raining outside!'
# another_string = 'It"s raining outside!'

long_string = """Это многострочная строка.
Она состоит из нескольких строк,
которые разделены переносами строк.
Также в этой строке можно использовать одинарные и двойные кавычки без экранирования."""

quote = """Это строка содержит "кавычки" внутри неё."""

zen = ("Явное лучше, чем неявное."
       "Простое лучше, чем сложное."
       "Сложное лучше, чем запутанное.")

zen_2 = "Явное лучше, чем неявное." \
        "Простое лучше, чем сложное." \
        "Сложное лучше, чем запутанное."

zen_of_python = (
    "Явное лучше, чем неявное.\n"
    "Простое лучше, чем сложное.\n"
    "Сложное лучше, чем запутанное.\n"
)

# -----------------------------
# Логические и физические строки

two_sum = 2 + 5

two_sum_2 = (
        2 + 5
)

x = 10; y = 20; z = 30

# -----------------------------
# Отступы

if x > 0 and y < 10 and z == 3:
    print("Условие выполнено!")

    if y == 5:
        print("abc")
        if z == 55:
            print("egh")

    print("egh")

print("egh")

# if (x > 0 and y < 10 and z == 3) {
#     print("Условие выполнено!")
# }

# -----------------------------
# Преобразование типов часть 1

# n = 10
# n_2 = "10"
# n_3 = 10

n = 10
n_2 = str(n)  # n_2 = "10"
n_3 = int(n_2)  # n_3 = 10

a = int("1053266")  # 1053266
b = str(12345)  # "12345"
c = float("3.14")  # 3.14

# int("3.14")  # ValueError

d = int(float("3.14"))  # 3
e = int(9.9993346)  # 9

int(101)  # 101
str("abc")  # "abc"
float(3.14)  # 3.14

float("13125246")  # 13125246.0

# int("abc")  # ValueError
# float("def")  # ValueError

a = 5
b = str(a)  # b будет равно "5"
c = str(3.14)  # c будет равно "3.14"
d = str(True)  # d будет равно "True"
e = str(None)  # e будет равно "None"

# -----------------------------

# 10543 значение
# str => преобразовать_к_строке

# какой-то-объект = преобразовать_к_строке(значение)
#
# печатать(какой-то-объект)  # "10543"

