"""Автопроверка задания 3.2. Запуск: python check_3_2.py"""
from _common import Report, load

out_of_range, rate, moving_average = load("task_3_2", "out_of_range", "rate", "moving_average")
r = Report("Задание 3.2: out_of_range, rate, moving_average")
P = [1.20, 1.31, 1.45, 1.52, 9.80, 1.54, 1.49, 1.40, 1.28, -6.10, 1.05, 0.93]
r.check("данные задания: out_of_range(P, -5, 5)", lambda: out_of_range(P, -5, 5), [4, 9])
r.check("данные задания: rate(P, 0.02)", lambda: rate(P, 0.02), [(b - a) / 0.02 for a, b in zip(P, P[1:])])
r.check("данные задания: moving_average(P, 3)", lambda: moving_average(P, 3), [sum(P[i:i + 3]) / 3 for i in range(10)])
r.check("границы входят в диапазон", lambda: out_of_range([-5.0, 5.0, -5.01, 5.01], -5, 5), [2, 3])
r.check("постоянный сигнал: производная нулевая", lambda: rate([2.0, 2.0, 2.0], 0.1), [0.0, 0.0])
r.check("линейный рост 1 град за шаг 0.5 с", lambda: rate([0.0, 1.0, 2.0], 0.5), [2.0, 2.0])
r.check("окно 1 — ряд без изменений", lambda: moving_average([1.0, 2.0, 4.0], 1), [1.0, 2.0, 4.0])
r.check("окно равно длине ряда — одно значение", lambda: moving_average([1.0, 2.0, 6.0], 3), [3.0])
r.finish()
