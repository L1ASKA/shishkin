import itertools
import time
#IT-предприятие набирает сотрудников: 2 тимлида, 2 проджек-менеджера, 3 синьера, 3 мидла, 4 юниора. Сформировать все возможные варианты заполнения вакантных мест, если имеются 16 претендентов.


# Основная функция для генерации всех возможных вариантов с ограничениями
def generate_employee_combinations(candidates, roles):
    all_combinations = []  # Список для хранения всех комбинаций

    # Генерируем комбинации для каждой роли
    for role, count in roles:
        # Формируем комбинацию ролей
        current_combinations = list(itertools.combinations(candidates, count))  # Комбинации для текущей роли
        all_combinations.extend(current_combinations)  # Добавляем все комбинации к общему списку

    # Применим ограничения: например, два тимлида и проджект-менеджера не могут быть одними и теми же кандидаты
    valid_combinations = []
    for combination in all_combinations:
        if (combination.count('Team Lead') <= 2 and
                combination.count('Project Manager') <= 2):
            valid_combinations.append(combination)

    return valid_combinations


# Главная функция
def main():
    candidates = ['Candidate 1', 'Candidate 2', 'Candidate 3', 'Candidate 4',
                  'Candidate 5', 'Candidate 6', 'Candidate 7', 'Candidate 8',
                  'Candidate 9', 'Candidate 10', 'Candidate 11', 'Candidate 12',
                  'Candidate 13', 'Candidate 14', 'Candidate 15', 'Candidate 16']  # 16 кандидатов
    roles = [('Team Lead', 2), ('Project Manager', 2), ('Senior', 3), ('Middle', 3), ('Junior', 4)]

    start_time = time.time()  # Начинаем замер времени
    combinations = generate_employee_combinations(candidates, roles)  # Генерируем варианты
    print("Найдено вариантов:", len(combinations))  # Выводим количество найденных вариантов
    print("Время выполнения: %s секунд" % (time.time() - start_time))  # Выводим время выполнения


if __name__ == "__main__":
    main()  # Запускаем программу