"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

month_num = int(input('Введите номер месяца: '))
month_list = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
month_dict = {(3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень', (12, 1, 2): 'Зима'}

if month_num in month_list[0]:
    print('Весна')
elif month_num in month_list[1]:
    print('Лето')
elif month_num in month_list[2]:
    print('Осень')
else:
    print('Зима')

# print(month_dict.get(month_dict.keys()))
print(month_dict.keys(month_num))
