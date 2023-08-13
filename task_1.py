"""
Создайте модуль и напишите в нём функцию,
которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует
Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
import datetime


def check_date(date_str: str) -> bool:
    try:
        date_ = datetime.datetime.strptime(date_str, '%d.%m.%Y')
    except ValueError:
        return False
    else:
        leap_year = _leap_year(date_str.split(".")[2])
        print("високоснный" if leap_year else "не високоснный")
        return True


def _leap_year(year_str: str) -> bool:
    year = int(year_str)
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


print(check_date("29.02.2024"))
