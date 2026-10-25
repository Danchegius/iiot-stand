"""Автопроверка задания 4.1. Запуск: python check_4_1.py"""
from _common import Report, load

normalize = load("task_4_1", "normalize")
r = Report("Задание 4.1: normalize (версия с try/except)")
cases = [(" 12,5 ", 12.5), ("13.0", 13.0), ("-0,75", -0.75), ("####", None), ("", None), ("  7 ", 7.0),
         ("N/A", None), ("1 250,3", 1250.3), (" 0 ", 0.0), ("abc", None), ("+3,5", 3.5)]


def exact(got, expected):
    if expected is None:
        return got is None
    return isinstance(got, float) and got == expected


for raw, expected in cases:
    r.check(repr(raw), lambda x=raw: normalize(x), expected, compare=exact,
            hint=lambda got: "Функция должна возвращать float, а не строку" if isinstance(got, str) else None)
r.finish()
