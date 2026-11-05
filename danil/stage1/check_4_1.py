"""Автопроверка задания 4.1. Запуск: python check_4_1.py"""
import math

from _common import Report, load

to_degrees = load("task_4_1", "to_degrees")
r = Report("Задание 4.1: to_degrees (версия с try/except)")
cases = [("12.5 deg", 12.5), ("0,5 rad", math.degrees(0.5)), ("  -3 deg ", -3.0), ("45deg", 45.0),
         ("-0,25 RAD", math.degrees(-0.25)), ("NaN deg", None), ("12.5 grad", None), ("", None),
         ("1e-1 rad", math.degrees(0.1)), ("+2 deg", 2.0), ("deg", None), ("12.5", None), ("nan rad", None)]


def hint(got):
    if isinstance(got, float) and math.isnan(got):
        return "Функция вернула nan. Для недостоверного отсчёта нужно None — посмотри функцию math.isnan."
    if isinstance(got, str):
        return "Функция должна возвращать float, а не строку"
    return None


for raw, expected in cases:
    r.check(repr(raw), lambda x=raw: to_degrees(x), expected, hint=hint)
r.finish()
