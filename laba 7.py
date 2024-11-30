import itertools
import time
import tkinter as tk
from tkinter import scrolledtext
#Требуется для своего варианта второй части л.р.
# №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
# Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.

# Основная функция для генерации всех возможных вариантов с ограничениями
def generate_employee_combinations(candidates, roles):
    all_combinations = []  # Список для хранения всех комбинаций

    # Генерируем комбинации для каждой роли
    for role, count in roles:
        # Формируем комбинацию ролей
        current_combinations = list(itertools.combinations(candidates, count))  # Комбинации для текущей роли
        all_combinations.extend(current_combinations)  # Добавляем все комбинации к общему списку

    # Применим ограничения
    valid_combinations = []
    for combination in all_combinations:
        if (combination.count('Team Lead') <= 2 and
                combination.count('Project Manager') <= 2):
            valid_combinations.append(combination)

    return valid_combinations


class CombinationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генерация комбинаций кандидатов")

        self.label = tk.Label(root, text="Нажмите кнопку, чтобы сгенерировать комбинации:")
        self.label.pack(pady=10)

        self.generate_button = tk.Button(root, text="Сгенерировать", command=self.generate_combinations)
        self.generate_button.pack(pady=10)

        self.output_window = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_window.pack(pady=10)

    def generate_combinations(self):
        candidates = ['Candidate 1', 'Candidate 2', 'Candidate 3', 'Candidate 4',
                      'Candidate 5', 'Candidate 6', 'Candidate 7', 'Candidate 8',
                      'Candidate 9', 'Candidate 10', 'Candidate 11', 'Candidate 12',
                      'Candidate 13', 'Candidate 14', 'Candidate 15', 'Candidate 16']  # 16 кандидатов
        roles = [('Team Lead', 2), ('Project Manager', 2), ('Senior', 3), ('Middle', 3), ('Junior', 4)]

        start_time = time.time()  # Начинаем замер времени
        combinations = generate_employee_combinations(candidates, roles)  # Генерируем варианты
        execution_time = time.time() - start_time  # Время выполнения

        # Очищаем предыдущее содержимое окна вывода
        self.output_window.delete(1.0, tk.END)

        # Выводим результаты
        self.output_window.insert(tk.END, f"Найдено вариантов: {len(combinations)}\n")
        self.output_window.insert(tk.END, f"Время выполнения: {execution_time:.2f} секунд\n\n")
        self.output_window.insert(tk.END, "Комбинации кандидатов:\n")
        for combo in combinations:
            self.output_window.insert(tk.END, f"{combo}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = CombinationApp(root)
    root.mainloop()