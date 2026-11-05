"""Автопроверка задания 4.2. Запуск: python check_4_2.py"""
from _common import Report, load

validate, BadSampleError, OutOfRangeError, UnknownChannelError = load(
    "task_4_2", "validate", "BadSampleError", "OutOfRangeError", "UnknownChannelError")
r = Report("Задание 4.2: validate")
for cls in (BadSampleError, OutOfRangeError, UnknownChannelError):
    r.check(f"{cls.__name__} — это класс исключения", lambda c=cls: isinstance(c, type) and issubclass(c, Exception), True)
ok_cases = [("ANG_PITCH", "12,5", 12.5), ("GYRO_Y", " -500 ", -500.0), ("ACC_Z", "16", 16.0),
            ("ANG_ROLL", "-180", -180.0), ("ACC_X", "0", 0.0)]
for ch, raw, expected in ok_cases:
    r.check(f"{ch}, {raw!r}", lambda c=ch, x=raw: validate(c, x), expected)
err_cases = [
    ("ANG_PITCH", "NaN", BadSampleError), ("GYRO_Y", "", BadSampleError), ("ACC_Z", " nan ", BadSampleError),
    ("ANG_YAW", "---", BadSampleError), ("ANG_PITCH", "180,5", OutOfRangeError), ("GYRO_X", "-500,1", OutOfRangeError),
    ("ACC_Y", "16.01", OutOfRangeError), ("MAG_X", "10", UnknownChannelError), ("ANG_PITCH", "12x", ValueError),
]
for ch, raw, exc in err_cases:
    r.check(f"{ch}, {raw!r}", lambda c=ch, x=raw: validate(c, x), raises=exc)
r.finish()
