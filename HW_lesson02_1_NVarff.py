# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# создай элементы как переменные. дай им названия
# потом создай список из элементов(переменных)
# далее через print(type) и что то еще выведи проверку типа данных в списке на экран

a = 256  # int
b = "Hello"  # str
c = 25.5  # float
d = b"Hello"  # bytes
f = {"name": "John", "age": 10}  # dict
list_of_elements = [a, b, c, d, f]
print(list_of_elements)
print(type(list_of_elements))

for element in list_of_elements:
    print(type(element))

    # The end DONE
for element in list_of_elements:
    print(f"Тип данных списка {type(element)}")  # хочу задать формат вывода