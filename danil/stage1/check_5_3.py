"""Автопроверка задания 5.3. Запуск: python check_5_3.py"""
from _common import Report, load

find_gaps, actual_rate = load("task_5_3", "find_gaps", "actual_rate")
r = Report("Задание 5.3: find_gaps и actual_rate")
D = "19.10.2026 08:15:42."
S1 = [D + ms for ms in ["000", "020", "040", "120", "140", "160", "300", "320"]]
S2 = [D + ms for ms in ["000", "021", "040", "069", "100", "120"]]
S3 = ["19.10.2026 23:59:59.960", "19.10.2026 23:59:59.980", "20.10.2026 00:00:00.000",
      "20.10.2026 00:00:00.020", "21.10.2026 00:00:00.520"]

r.check("первый набор: find_gaps", lambda: find_gaps(S1, 0.02), [(D + "040", 0.08), (D + "160", 0.14)])
r.check("первый набор: actual_rate", lambda: actual_rate(S1), 21.875)
r.check("джиттер не пропуск, а 31 мс уже пропуск", lambda: find_gaps(S2, 0.02), [(D + "069", 0.031)])


def hint3(got):
    if isinstance(got, list) and not got:
        return "Пропуск длиной больше суток не найден. Посмотри «Типичные ошибки главы 5» про .seconds."
    return None


r.check("переход через полночь и перерыв больше суток", lambda: find_gaps(S3, 0.02),
        [("20.10.2026 00:00:00.020", 86400.5)], hint=hint3)
r.check("одна метка: actual_rate", lambda: actual_rate([D + "000"]), None)
r.check("пустой список: find_gaps", lambda: find_gaps([], 0.02), [])
r.finish()
