"""Общая часть автопроверок. Этот файл не нужно менять или запускать."""
import importlib
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

OK, FAIL = "[+]", "[-]"


def load(module_name, *names):
    """Импортирует решение и возвращает нужные объекты по именам."""
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as err:
        if err.name == module_name:
            print(f"Не найден файл {module_name}.py рядом с проверкой.")
            print(f"Положите решение в папку {HERE} под именем {module_name}.py")
        else:
            print(f"Решение импортирует модуль, которого нет: {err.name}")
        sys.exit(1)
    except Exception as err:
        print(f"Файл {module_name}.py падает уже при импорте: {type(err).__name__}: {err}")
        print('Проверьте, что код для запуска стоит под if __name__ == "__main__":')
        sys.exit(1)
    found = []
    for name in names:
        if not hasattr(module, name):
            print(f"В файле {module_name}.py нет объекта {name}. Проверьте имя по заданию.")
            sys.exit(1)
        found.append(getattr(module, name))
    return found[0] if len(found) == 1 else found


def same(a, b):
    """Сравнение с допуском для дробных чисел."""
    if isinstance(a, float) or isinstance(b, float):
        try:
            return math.isclose(float(a), float(b), rel_tol=1e-9, abs_tol=1e-9)
        except (TypeError, ValueError):
            return False
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return type(a) is type(b) and len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b and type(a) is type(b)


class Report:
    def __init__(self, title):
        self.title, self.passed, self.total = title, 0, 0
        print(title)

    def check(self, label, func, expected=None, raises=None, compare=same, hint=None):
        """Вызывает func() и сравнивает результат с ожидаемым или проверяет тип исключения."""
        self.total += 1
        try:
            got = func()
        except Exception as err:
            if raises and isinstance(err, raises):
                self.passed += 1
                print(f"  {OK} {label}  ->  {type(err).__name__}")
            else:
                want = f"исключение {raises.__name__}" if raises else repr(expected)
                print(f"  {FAIL} {label}  ->  ожидалось {want}, а функция упала: {type(err).__name__}: {err}")
            return
        if raises:
            print(f"  {FAIL} {label}  ->  ожидалось исключение {raises.__name__}, а функция вернула {got!r}")
            return
        if compare(got, expected):
            self.passed += 1
            print(f"  {OK} {label}  ->  {got!r}")
        else:
            print(f"  {FAIL} {label}  ->  ожидалось {expected!r}, получено {got!r}")
            if hint:
                extra = hint(got)
                if extra:
                    print(f"      {extra}")

    def finish(self):
        print()
        if self.passed == self.total:
            print(f"Итог: {self.passed} из {self.total}. Все проверки пройдены, можно открывать pull request.")
        else:
            print(f"Итог: {self.passed} из {self.total}. Разберите строки с {FAIL} и запустите проверку снова.")
