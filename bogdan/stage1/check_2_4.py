"""Автопроверка задания 2.4. Запуск: python check_2_4.py"""
from _common import Report, load

count_events, max_high = load("task_2_4", "count_events", "max_high")
r = Report("Задание 2.4: count_events и max_high")

LOG = """19.10.2026 08:15:42 | KTP2.TT_101.PV | HIGH | 92,7
19.10.2026 08:17:03 | KTP2.TT_101.PV | NORMAL | 88,1
19.10.2026 09:02:11 | NS1.LT_12.PV | LOW | 0,35
19.10.2026 09:40:55 | NS1.LT_12.PV | NORMAL | 1,10
19.10.2026 10:05:20 | KTP2.TT_101.PV | HIGH | 93,4"""

LOG2 = """
20.10.2026 00:01:00 | K1.PT_3.PV | NORMAL | 2,40
20.10.2026 01:10:00 | K1.PT_3.PV | HIGH | 3,55

20.10.2026 01:12:00 | K1.PT_3.PV | HIGH | 3,61
20.10.2026 02:00:00 | K1.TT_9.PV | LOW | 11,0
20.10.2026 03:00:00 | K1.FT_1.PV | NORMAL | 40,0
20.10.2026 04:30:00 | K1.TT_9.PV | HIGH | 101,25
"""

r.check("журнал из задания: count_events", lambda: count_events(LOG),
        {"KTP2.TT_101.PV": {"HIGH": 2, "LOW": 0}, "NS1.LT_12.PV": {"HIGH": 0, "LOW": 1}})
r.check("журнал из задания: max_high", lambda: max_high(LOG), 93.4)
r.check("второй журнал с пустыми строками: count_events", lambda: count_events(LOG2),
        {"K1.PT_3.PV": {"HIGH": 2, "LOW": 0}, "K1.TT_9.PV": {"HIGH": 1, "LOW": 1}, "K1.FT_1.PV": {"HIGH": 0, "LOW": 0}})
r.check("второй журнал: max_high", lambda: max_high(LOG2), 101.25)
r.check("журнал без HIGH: max_high", lambda: max_high("20.10.2026 03:00:00 | K1.FT_1.PV | LOW | 4,0"), None)
r.check("пустой журнал: count_events", lambda: count_events(""), {})
r.finish()
