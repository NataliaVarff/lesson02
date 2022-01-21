# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

My_input = ("Today is the best day ever").split( ) # для изучения и самопроверки
print(My_input)
for el in (My_input):
     print(el)

# Решение
Input_String = (input("Введите 5 любых слов")).split( )
#print(type(My_String))
print(Input_String)
for i,el in enumerate(Input_String, start = 1):
     print(i,el[0:10])





     # if len(el) >= 9:
     #     print(i,el[0:9])

    #print(String.index(String, 0, len(String)))
