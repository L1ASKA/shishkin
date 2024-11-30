import time
"4.	F(x<2) = 3; F(n) = (-1)n*(F(n-1)/n! + F(n-5) /(2n)!)"
max_n = 15

# Функция для вычисления факториала
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Заголовок для вывода
print(f"{'n':<10}{'Recursive Time (s)':<25}{'Iterative Time (s)':<25}")

for n in range(max_n + 1):
    # Рекурсивное вычисление F(n)
    start_time = time.time()

    if n < 2:
        recursive_result = 3
    else:
        def recursive_helper(n):
            if n < 2:
                return 3
            else:
                last_value = recursive_helper(n - 1) / factorial(n)
                five_value = recursive_helper(n - 5) / factorial(2 * n) if n >= 5 else 0
                return (-1) * n * (last_value + five_value)

        recursive_result = recursive_helper(n)

    recursive_time = time.time() - start_time

    # Итеративное вычисление F(n)
    start_time = time.time()

    if n < 2:
        iterative_result = 3
    else:
        results = [0] * (n + 1)
        results[0] = 3

        for i in range(1, n + 1):
            if i < 2:
                results[i] = 3
            else:
                last_value = results[i - 1] / factorial(i) if i - 1 >= 0 else 0
                five_value = results[i - 5] / factorial(2 * i) if i >= 5 else 0
                results[i] = (-1) * i * (last_value + five_value)

        iterative_result = results[n]

    iterative_time = time.time() - start_time

    # Вывод результатов
    print(f"{n:<10}{recursive_time:<25}{iterative_time:<25}")
