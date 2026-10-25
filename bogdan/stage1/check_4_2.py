"""Автопроверка задания 4.2. Запуск: python check_4_2.py"""
from _common import Report, load

validate, BadQualityError, OutOfRangeError, UnknownTagError = load(
    "task_4_2", "validate", "BadQualityError", "OutOfRangeError", "UnknownTagError")
r = Report("Задание 4.2: validate")

for cls in (BadQualityError, OutOfRangeError, UnknownTagError):
    r.check(f"{cls.__name__} — это класс исключения", lambda c=cls: isinstance(c, type) and issubclass(c, Exception), True)

ok_cases = [("TT_101", "85,4", 85.4), ("PT_204", " 2.5 ", 2.5), ("LT_12", "5", 5.0), ("TT_1", "-50", -50.0), ("PT_7", "0", 0.0)]
for tag, raw, expected in ok_cases:
    r.check(f"{tag}, {raw!r}", lambda t=tag, x=raw: validate(t, x), expected)

err_cases = [
    ("TT_101", "####", BadQualityError), ("PT_1", "", BadQualityError), ("LT_3", " N/A ", BadQualityError),
    ("TT_5", "BAD", BadQualityError), ("LT_12", "5,01", OutOfRangeError), ("PT_2", "-0,1", OutOfRangeError),
    ("TT_8", "200,5", OutOfRangeError), ("QT_5", "10", UnknownTagError), ("TT_101", "12x", ValueError),
]
for tag, raw, exc in err_cases:
    r.check(f"{tag}, {raw!r}", lambda t=tag, x=raw: validate(t, x), raises=exc)
r.finish()
