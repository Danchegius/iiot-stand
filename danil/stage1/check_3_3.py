"""Автопроверка задания 3.3. Запуск: python check_3_3.py"""
from _common import Report, load

rank_sensors = load("task_3_3", "rank_sensors")
r = Report("Задание 3.3: rank_sensors")
r.check("разный шум", lambda: rank_sensors({"GYRO_X": 0.031, "GYRO_Y": 0.018, "ACC_Z": 0.044}), ["GYRO_Y", "GYRO_X", "ACC_Z"],
        hint=lambda got: "Похоже, порядок обратный: нужен от самого тихого к самому шумному" if got == ["ACC_Z", "GYRO_X", "GYRO_Y"] else None)
r.check("равный шум идёт по алфавиту",
        lambda: rank_sensors({"GYRO_Z": 0.02, "ACC_X": 0.05, "GYRO_A": 0.02, "BARO": 0.01, "ACC_B": 0.02}),
        ["BARO", "ACC_B", "GYRO_A", "GYRO_Z", "ACC_X"])
r.check("все равны", lambda: rank_sensors({"c": 0.1, "a": 0.1, "b": 0.1}), ["a", "b", "c"])
r.check("пустой словарь", lambda: rank_sensors({}), [])
r.finish()
