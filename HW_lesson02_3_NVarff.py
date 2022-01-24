# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# решение через if else
Month = int(input("Введите номер любого месяца календарного года >>"))

if Month > 2 and Month < 6:
        print("This month relates to Sping")
elif Month > 5 and Month < 9:
    print("This month relates to Summer")
elif Month > 8 and Month < 12:
    print("This month relates to Autumn")
elif Month ==1 or Month == 2 or Month == 12:
    print("This month relates to Winter")
else:
    print("This month is out of calender year")

### решение через список и словарь
month_input = int(input("Введите номер любого месяца календарного года >>"))
if 12 >= month_input >= 1:
    season_dict = {1:"Winter",
                   2:"Winter",
                   3:"Spring",
                   4:"Spring",
                   5:"Spring",
                   6:"Summer",
                   7:"Summer",
                   8:"Summer",
                   9:"Autumm",
                   10:"Autumm",
                   11:"Autumm",
                   12:"Winter"}
    season_list = list(season_dict.values())
   # print(season_list)
    print(f"This month relates to {season_list[month_input-1]}")
else:
    print("This month is out of calender year")





