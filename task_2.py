"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

import datetime
from sys import argv


def check_date(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, '%d.%m.%Y')
    except ValueError:
        return False
    else:
        leap_year = _leap_year(date_str.split(".")[2])
        print("год високоснный" if leap_year else "год не високоснный")
        return True


def _leap_year(year_str: str) -> bool:
    year = int(year_str)
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


if __name__ == "__main__":
    if len(argv) > 1:
        print("дата существует" if check_date(argv[1]) else "дата не существует")
