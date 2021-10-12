import os, sys
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def save(name='', fmt='png'): # Сохранение пути для графика
    pwd = os.getcwd()
    list_path_to_worker_file = (os.path.dirname(os.path.realpath(sys.argv[0]))).split('/')
    iPath = '/'.join(list_path_to_worker_file[:-2]) + "/function_modeling/graphs/"
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt))
    os.chdir(pwd)


def create_time_period_with_step(period, step): # Создание списка от datetime.now() до datetime.now() - period, с шагом step
    time_period_with_step = []
    current_date = datetime.now()
    past_date = current_date - timedelta(days=period)
    while current_date > past_date:
        time_period_with_step.append(past_date)
        try:
            past_date += timedelta(hours=step)
        except OverflowError:
            return "date value out of range"
    time_period_with_step.append(current_date)
    return time_period_with_step


def get_path(name, fmt='png'): # Генерация пути для графика в БД
    return "graphs/" + '{}.{}'.format(str(name), fmt)