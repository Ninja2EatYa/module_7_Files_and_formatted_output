print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2=42))
print('Волшебники данных решили задачи за {team1_time} c!'.format(team1_time=18015.2))
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды Мастера кода!'
print(f'Результат битвы: {challenge_result}')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


def challenge_result(score_1, score_2, team1_time, team2_time, tasks_total, time_avg):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    print('challenge_result:', result)


def time_avg(team1_time, team2_time, tasks_total):
    return f'time_avg: {(team1_time + team2_time) / tasks_total}'


print('')
challenge_result(40, 42, 1552.512, 2153.31451, 82, 45.2, )
print(time_avg(1552.512, 2153.31451, 82))
