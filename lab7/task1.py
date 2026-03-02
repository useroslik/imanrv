# Функция add(a, b) — возвращает сумму двух чисел.
def add(a, b):
    return a + b

# Функция power(a, n=2) — возводит число в степень (по умолчанию во вторую).
def power(a, n=2):
    return a ** n

# Функция sum_all(*args) — возвращает сумму произвольного количества чисел.
def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total

# Пример использования функций (для проверки)
if __name__ == "_main_":
    # Проверка add
    print("Сумма 5 и 3:", add(5, 3))

    # Проверка power (с одним параметром и с двумя)
    print("2 в квадрате (по умолчанию):", power(2))
    print("2 в кубе (n=3):", power(2, 3))

    # Проверка sum_all
    print("Сумма чисел 1, 2, 3, 4, 5:", sum_all(1, 2, 3, 4, 5))
    print("Сумма чисел 10 и 20:", sum_all(10, 20))