#МОДУЛЬ 5

year_pyshkin = 1799  #др Пушкина
day_pushkin=6

year_users = int(input('Введите год рождения А.С. Пушкина: '))
while year_users!=year_pyshkin:
    year_users=int(input('Ошибка, повторите ввод: '))
day_user=int(input('Верно!, теперь укажите день рождения: '))
while day_user!=day_pushkin:
    day_user = int(input('Ошибка, повторите ввод: '))
print ('Успех!')






