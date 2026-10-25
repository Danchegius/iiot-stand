"""Автопроверка задания 2.1. Запуск: python check_2_1.py"""
from _common import Report, load

parse_tag = load("task_2_1", "parse_tag")
r = Report("Задание 2.1: parse_tag")
cases = [
    ("KTP2.TT_101.PV", ("KTP2", "TT", "101", "температура", "PV")),
    ("KTP2.PT_204.PV", ("KTP2", "PT", "204", "давление", "PV")),
    ("NS1.LT_12.SP", ("NS1", "LT", "12", "уровень", "SP")),
    ("NS1.FT_7.PV", ("NS1", "FT", "7", "расход", "PV")),
    ("KTP2.TT_102.SP", ("KTP2", "TT", "102", "температура", "SP")),
    ("VODOKANAL3.PT_1.PV", ("VODOKANAL3", "PT", "1", "давление", "PV")),
    ("K1.QT_55.PV", ("K1", "QT", "55", "неизвестно", "PV")),
]
for tag, expected in cases:
    r.check(repr(tag), lambda t=tag: parse_tag(t), expected,
            hint=lambda got: "Функция должна вернуть кортеж (tuple), а не список" if isinstance(got, list) else None)
r.finish()
