"""Автопроверка задания 5.2. Запуск: python check_5_2.py"""
import tempfile
from pathlib import Path

from _common import Report, load

read_any = load("task_5_2", "read_any")
r = Report("Задание 5.2: read_any")
TEXT = "Время;Тег;Значение\n19.10.2026 08:00:00;ТТ-101 температура подачи;85,4\n"

with tempfile.TemporaryDirectory() as tmp:
    for enc in ("utf-8", "utf-8-sig", "cp1251"):
        path = Path(tmp) / f"test_{enc}.csv"
        path.write_bytes(TEXT.encode(enc))

        def hint(got):
            if isinstance(got, str) and got.startswith("﻿"):
                return "В начале текста лишний невидимый символ '\\ufeff'. Перечитайте в справочнике, раздел 5.3, что такое utf-8-sig."
            return None

        r.check(f"файл в кодировке {enc}", lambda p=path: read_any(p), TEXT, hint=hint)
    r.check("путь передан строкой, а не Path", lambda: read_any(str(Path(tmp) / "test_cp1251.csv")), TEXT)
r.finish()
