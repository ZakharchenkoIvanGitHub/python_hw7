"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""

from for_task_2_3 import task_3
from random import randint


def generate_queens():
    queens_lst = []
    while len(queens_lst)<8:
        queen = (randint(1, 8), randint(1, 8))
        add_queen = True
        for queen_old in queens_lst:
            if queen == queen_old:
                add_queen = False
        if add_queen:
            queens_lst.append(queen)

    return queens_lst


def check_lst():
    find_lst = []
    while len(find_lst) < 4:
        lst_queens = generate_queens()

        if task_3.check_queens(lst_queens):
            find_lst.append(lst_queens)
            print(lst_queens)
    return find_lst


if __name__ == "__main__":
    print(check_lst())
