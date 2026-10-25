"""Автопроверка задания 2.2. Запуск: python check_2_2.py"""
from _common import Report, load

normalize = load("task_2_2", "normalize")
r = Report("Задание 2.2: normalize (версия на методах строк)")


def as_number(got, expected):
    if expected is None:
        return got is None
    if not isinstance(got, str):
        return False
    try:
        return float(got) == expected
    except ValueError:
        return False


cases = [(" 12,5 ", 12.5), ("13.0", 13.0), ("-0,75", -0.75), ("####", None), ("", None),
         ("  7 ", 7.0), ("N/A", None), ("1 250,3", 1250.3)]
for raw, expected in cases:
    want = None if expected is None else f"строка, которую float() превратит в {expected}"
    r.check(repr(raw), lambda x=raw: normalize(x), want,
            compare=lambda got, _w, e=expected: as_number(got, e),
            hint=lambda got: "Функция должна возвращать строку или None, а не число" if isinstance(got, (int, float)) else None)
r.finish()
