# МОДУЛЬ 6

# people_dict={'Гагарин':1934, 'Сталин':1878, 'Дрейк':1986, 'Дре':1965, 'Андропов':1914}
# -пока не придумал как при помощи словаря по красоте сделать


years_list = [1934, 1878, 1986, 1965, 1914, ['Гагарина', 'Сталина', 'Drake', 'dr.Dre', 'Андропова']]

good_answer = 0  # правильные ответы
bad_answer = 0  # ложные ответы
questions = 0  # кол-во вопросов

while True:
    for i in range(len(years_list) - 1):  # -1 чтобы цикл не проваливался во вложенный список
        tmp = int(input(f'Введи дату рождения {years_list[5][i]}: '))  # из вложенного списика смотрит кого угадать
        questions += 1
        if tmp == years_list[i]:
            good_answer += 1
        else:
            bad_answer += 1
    avg_good = good_answer / questions * 100
    avg_bad = bad_answer / questions * 100
    print(
        f'Правильных ответов: {good_answer}, Неправильных ответов: {bad_answer} \nПроцент верных ответов: {avg_good}, Процент неправильных ответов: {avg_bad}')
    print('Игра окончена, хотите повторить (да/нет)?:')
    ask = input()
    if ask == 'нет':
        break
    else:
        continue
