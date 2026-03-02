def sum_digits(n):
    """
    Рекурсивно вычисляет сумму цифр числа.
    """
    # Базовый случай: если число однозначное
    if n < 10:
        return n
    # Рекурсивный случай: последняя цифра + сумма остальных
    return n % 10 + sum_digits(n // 10)

# Тестирование
if __name__ == "_main_":
    print(f"sum_digits(1234) = {sum_digits(1234)}")  # 1+2+3+4 = 10
    print(f"sum_digits(9876) = {sum_digits(9876)}")  # 9+8+7+6 = 30
    print(f"sum_digits(5) = {sum_digits(5)}")        # 5
    print(f"sum_digits(0) = {sum_digits(0)}")        # 0