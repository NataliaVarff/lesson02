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





# not mine
# num = int(input("Введите номер месяца (от 1 до 12): "))
# if 12 >= num >= 1:
#     dict_months = {1: 'январь (зима) ',
#                    2: 'февраль (зима)',
#                    3: 'март (весна)',
#                    4: 'апрель (весна)',
#                    5: 'май (весна)',
#                    6: 'июнь (лето)',
#                    7: 'июль (лето)',
#                    8: 'август (лето)',
#                    9: 'сентябрь (осень)',
#                    10: 'октябрь (осень)',
#                    11: 'ноябрь (осень)',
#                    12: 'декабрь (зима)'}
#     list_months = list(dict_months.values())
#     print(f"Введенный номер соответствует месяцу: {list_months[num - 1]}")
# else:
#     print("Месяца с таким номером не существует")



#months_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(months_list)
#for i in months_list:

#ввести номер дня недели и получить название дня

Day_num = int(input("введите номер дня недели от 1 до 7"))
if 7 >= Day_num >=1:
    days_dict = {1:"Monday",
                 2:"Tuesday",
                 3:"Wednesday",
                 4:"Thursday",
                 5:"Friday",
                 6:"Saturday",
                 7:"Sunday" }
    days_list = list(days_dict.values())
    print(f"Номер дня соответствует наименованию {days_list[Day_num-1]}")