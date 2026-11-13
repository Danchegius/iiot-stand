"""Автопроверка задания 2.4. Запуск: python check_2_4.py"""
from _common import Report, load

count_events, max_sat = load("task_2_4", "count_events", "max_sat")
r = Report("Задание 2.4: count_events и max_sat")
LOG = """08:15:42.120 | GYRO_Y | SAT | 500,0
08:15:42.140 | GYRO_Y | OK | 498,2
08:15:42.160 | ACC_Z | DROP | 0
08:15:42.180 | ACC_Z | OK | 9,79
08:15:42.200 | ACC_Z | SAT | -16,0"""
LOG2 = """
09:00:00.000 | GYRO_X | OK | 12,0
09:00:00.020 | GYRO_X | SAT | -512,5

09:00:00.040 | GYRO_X | SAT | 511,0
09:00:00.060 | ANG_PITCH | DROP | 0
09:00:00.080 | ACC_X | OK | 0,98
09:00:00.100 | ANG_PITCH | DROP | 0
09:00:00.120 | ACC_X | SAT | 16,0
"""
r.check("журнал из задания: count_events", lambda: count_events(LOG),
        {"GYRO_Y": {"SAT": 1, "DROP": 0}, "ACC_Z": {"SAT": 1, "DROP": 1}})
r.check("журнал из задания: max_sat", lambda: max_sat(LOG), 500.0)
r.check("второй журнал с пустыми строками: count_events", lambda: count_events(LOG2),
        {"GYRO_X": {"SAT": 2, "DROP": 0}, "ANG_PITCH": {"SAT": 0, "DROP": 2}, "ACC_X": {"SAT": 1, "DROP": 0}})
r.check("второй журнал: max_sat (по модулю, со знаком)", lambda: max_sat(LOG2), -512.5,
        hint=lambda got: "Похоже, найден максимум без учёта модуля" if got == 511.0 else None)
r.check("журнал без SAT: max_sat", lambda: max_sat("09:00:00.000 | ACC_X | DROP | 0"), None)
r.check("пустой журнал: count_events", lambda: count_events(""), {})
r.finish()
