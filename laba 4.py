import re
"Вещественные числа, заключенные в кавычки (все виды). Кавычки не выводятся. Целая часть числа выводится словами."
## Функция для преобразования числа в слова
def number_to_words(n):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
             "шестнадцать", "семнадцать", "восемнадцать", "девятьнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот",
                "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 0:
        return "ноль"

    words = []

    if n >= 100:
        words.append(hundreds[n // 100])
        n %= 100
    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
    elif n >= 10:
        words.append(teens[n - 10])
        n = 0
    if n > 0:
        words.append(units[n])

    return ' '.join(filter(None, words))

# Чтение файла и обработка содержимого
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Регулярное выражение для поиска вещественных чисел в кавычках, включая отрицательные
    pattern = r'["\']([-+]?\d*\.\d+)["\']'
    matches = re.findall(pattern, content)

    for match in matches:
        # Определяем знак числа
        sign = ""
        if match.startswith('-'):
            sign = "минус "
        elif match.startswith('+'):
            match = match[1:]  # Убираем знак +

        integer_part = int(float(match))
        decimal_part = match.split('.')[-1]
        words = number_to_words(abs(integer_part))  # Преобразуем только абсолютное значение
        print(f"{sign}{words} {decimal_part}")

# Пример использования
if __name__ == "__main__":
    process_file('laba 4.txt')