"""Автопроверка задания 3.2. Запуск: python check_3_2.py"""
from _common import Report, load

out_of_range, jumps, mean_in_range = load("task_3_2", "out_of_range", "jumps", "mean_in_range")
r = Report("Задание 3.2: out_of_range, jumps, mean_in_range")

P = [2.41, 2.43, 2.40, 2.44, 3.12, 2.45, 2.42, 2.39, 1.85, 2.40, 2.41, 2.44]
r.check("данные задания: out_of_range(P, 2.0, 3.0)", lambda: out_of_range(P, 2.0, 3.0), [4, 8])
r.check("данные задания: jumps(P, 0.3)", lambda: jumps(P, 0.3), [3, 4, 7, 8])
r.check("данные задания: mean_in_range(P, 2.0, 3.0)", lambda: mean_in_range(P, 2.0, 3.0), 2.419)
B = [2.0, 3.0, 1.99, 3.01]
r.check("границы входят в уставки: out_of_range", lambda: out_of_range(B, 2.0, 3.0), [2, 3])
r.check("границы входят в уставки: mean_in_range", lambda: mean_in_range(B, 2.0, 3.0), 2.5)
r.check("скачок ровно на порог не считается", lambda: jumps([1.0, 1.5, 1.5, 1.0], 0.5), [])
r.check("скачок вниз тоже скачок", lambda: jumps([5.0, 4.0, 4.1], 0.5), [0])
r.check("всё в норме: out_of_range", lambda: out_of_range([2.5, 2.6], 2.0, 3.0), [])
r.finish()
