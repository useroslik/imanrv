# Рекурсивная версия
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Итерационная версия
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Тестирование
if __name__ == "_main_":
    print(f"5! = {factorial_recursive(5)} (рекурсивно)")
    print(f"5! = {factorial_iterative(5)} (итерационно)")