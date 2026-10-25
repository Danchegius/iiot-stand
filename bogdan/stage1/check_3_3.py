"""Автопроверка задания 3.3. Запуск: python check_3_3.py"""
from _common import Report, load

rank_tags = load("task_3_3", "rank_tags")
r = Report("Задание 3.3: rank_tags")
r.check("разные количества", lambda: rank_tags({"LT_12": 3, "TT_101": 7, "PT_204": 1}), ["TT_101", "LT_12", "PT_204"])
r.check("равные количества идут по алфавиту",
        lambda: rank_tags({"TT_101": 3, "LT_12": 7, "PT_204": 3, "FT_7": 1, "AT_2": 3}),
        ["LT_12", "AT_2", "PT_204", "TT_101", "FT_7"])
r.check("все равны", lambda: rank_tags({"b": 2, "c": 2, "a": 2}), ["a", "b", "c"])
r.check("пустой словарь", lambda: rank_tags({}), [])
r.finish()
