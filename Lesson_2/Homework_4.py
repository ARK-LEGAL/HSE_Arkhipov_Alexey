inn = int(input("Введите ИНН: "))
def check_inn_criteria(inn):
    """Проверяет, соответствует ли длина ИНН допустимым значениям (10 или 12 символов)."""
    return len(inn) == 10 or len(inn) == 12

def calculate_checksum_inn(inn):
    """Вычисляет контрольную сумму для ИНН."""
    if len(inn) == 10:
        coefficients = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum = sum(coefficients[i] * int(inn[i]) for i in range(9)) % 11 % 10
        return checksum == int(inn[9])
    elif len(inn) == 12:
        coefficients1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        coefficients2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum1 = sum(coefficients1[i] * int(inn[i]) for i in range(10)) % 11 % 10
        checksum2 = sum(coefficients2[i] * int(inn[i]) for i in range(11)) % 11 % 10
        return checksum1 == int(inn[10]) and checksum2 == int(inn[11])
    return False

def validate_inn(inn):
    """Валидирует ИНН."""
    if not inn.isdigit():
        return False
    if not check_inn_criteria(inn):
        return False
    return calculate_checksum_inn(inn)

# Пример использования:
inn = "123456789012"
print(validate_inn(inn))  # Вывод: True или False в зависимости от корректности ИНН
