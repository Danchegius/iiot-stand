"""Автопроверка задания 2.1. Запуск: python check_2_1.py"""
from _common import Report, load

parse_packet = load("task_2_1", "parse_packet")
r = Report("Задание 2.1: parse_packet")
cases = [
    ("T=0.120;PITCH=12.50;ROLL=-3.25;Q=OK", {"t": 0.12, "pitch": 12.5, "roll": -3.25, "q": "OK"}),
    (" T = 0.140 ; PITCH = 12,61 ; ROLL=-3.30;Q=OK; ", {"t": 0.14, "pitch": 12.61, "roll": -3.3, "q": "OK"}),
    ("T=0.160;PITCH=12.70;Q=LOST", {"t": 0.16, "pitch": 12.7, "q": "LOST"}),
    ("T=1.5;W_X=-0,05;W_Y=3;YAW=180.0;Q=OK", {"t": 1.5, "w_x": -0.05, "w_y": 3.0, "yaw": 180.0, "q": "OK"}),
    ("T=0.000", {"t": 0.0}),
]
for line, expected in cases:
    r.check(repr(line), lambda s=line: parse_packet(s), expected,
            hint=lambda got: "Числа должны быть float, а не строками" if isinstance(got, dict) and any(isinstance(v, str) for k, v in got.items() if k != "q") else None)
r.finish()
