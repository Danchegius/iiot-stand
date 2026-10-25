"""Автопроверка задания 5.3. Запуск: python check_5_3.py"""
from _common import Report, load

alarm_durations = load("task_5_3", "alarm_durations")
r = Report("Задание 5.3: alarm_durations")

LOG = """19.10.2026 08:15:42 | KTP2.TT_101.PV | HIGH | 92,7
19.10.2026 08:17:03 | KTP2.TT_101.PV | NORMAL | 88,1
19.10.2026 09:02:11 | NS1.LT_12.PV | LOW | 0,35
19.10.2026 09:40:55 | NS1.LT_12.PV | NORMAL | 1,10
19.10.2026 10:05:20 | KTP2.TT_101.PV | HIGH | 93,4"""

LOG2 = """19.10.2026 23:50:00 | K1.TT_9.PV | HIGH | 101
20.10.2026 00:05:30 | K1.TT_9.PV | HIGH | 103
20.10.2026 00:20:00 | K1.TT_9.PV | NORMAL | 95
20.10.2026 01:00:00 | K1.PT_3.PV | NORMAL | 2,4
20.10.2026 02:00:00 | K1.TT_9.PV | LOW | 10
20.10.2026 02:00:45 | K1.TT_9.PV | NORMAL | 50
20.10.2026 03:00:00 | K1.PT_3.PV | LOW | 0,5
21.10.2026 10:00:00 | K2.LT_1.PV | HIGH | 4,9
22.10.2026 10:00:10 | K2.LT_1.PV | NORMAL | 3,0"""

r.check("журнал из задания", lambda: alarm_durations(LOG),
        ({"KTP2.TT_101.PV": 81.0, "NS1.LT_12.PV": 2324.0}, {"KTP2.TT_101.PV": "19.10.2026 10:05:20"}))


def hint2(got):
    try:
        if abs(got[0].get("K2.LT_1.PV", 0) - 10) < 1:
            return "Для K2.LT_1.PV получилось 10 секунд вместо суток с лишним. Посмотрите «Типичные ошибки главы 5» про .seconds."
    except Exception:
        pass
    return None


r.check("переход через полночь, повторный HIGH, авария длиной больше суток", lambda: alarm_durations(LOG2),
        ({"K1.TT_9.PV": 1845.0, "K2.LT_1.PV": 86410.0}, {"K1.PT_3.PV": "20.10.2026 03:00:00"}), hint=hint2)
r.check("пустой журнал", lambda: alarm_durations(""), ({}, {}))
r.finish()
