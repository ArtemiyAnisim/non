months = {
        1: 'Январе',
        2: 'Феврале',
        3: 'Марте',
        4: 'Апреле',
        5: 'Мае',
        6: 'Июне',
        7: 'Июле',
        8: 'Августе',
        9: 'Сентябре',
        10: 'Октябре',
        11: 'Ноябре',
        12: 'Декабре'
    }


def season_events(number_of_month):
   if not isinstance(number_of_month, int) and 1 <= number_of_month <= 12:
        print('Введите номер месяца')
        return
   if number_of_month in range(3, 6):
    print(f'Вы родились в {months[number_of_month]}. Птицы пели прекрасные песни')
   elif number_of_month in range(6, 9):
           print(f'Вы родились в {months[number_of_month]}. Солнце светило ярче чем когда-либо')
   elif number_of_month in range(9, 12):
     print(f'Вы родились в {months[number_of_month]}. Урожай был невероятным')
   else:
        print(f'Вы родились в {months[number_of_month]}. За окном падал белый снег')
