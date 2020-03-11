import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    """
    Алгоритм работает по принципу бинарного поиска. https://ru.wikipedia.org/wiki/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA
    """
    left_boarder=1;
    right_boarder=100;
    count = 1 #начинаем с 1-ой попытки
    predict = np.random.randint(1,100)
    repeat_arr=[]
    while number != predict:
        count+=1
        if number > predict:
            left_boarder=predict 
        elif number < predict: 
            right_boarder=predict
        repeat_arr.append(predict)
        predict = int((right_boarder-left_boarder)/2)+left_boarder
        if predict in repeat_arr: #для случая когда загаданное число больше на 1 предполагаемого, чтобы не было зацикливания вводим данную проверку
            predict+=1
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v3)