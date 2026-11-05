"""Автопроверка задания 2.2. Запуск: python check_2_2.py"""
import math

from _common import Report, load

to_degrees = load("task_2_2", "to_degrees")
r = Report("Задание 2.2: to_degrees (версия на методах строк)")
cases = [("12.5 deg", 12.5), ("0,5 rad", math.degrees(0.5)), ("  -3 deg ", -3.0), ("45deg", 45.0),
         ("-0,25 RAD", math.degrees(-0.25)), ("3.14159rad", math.degrees(3.14159)),
         ("NaN deg", None), ("12.5 grad", None), ("", None)]
for raw, expected in cases:
    r.check(repr(raw), lambda x=raw: to_degrees(x), expected,
            hint=lambda got: "Функция должна возвращать float, а не строку" if isinstance(got, str) else None)
r.finish()
