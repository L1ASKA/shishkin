import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class Triangle:
    def __init__(self, A, B, C):
        self.A = A  # координаты точки A (x, y)
        self.B = B  # координаты точки B (x, y)
        self.C = C  # координаты точки C (x, y)

    def draw(self, canvas):
        """Рисует треугольник на заданном канвасе."""
        canvas.create_polygon(self.A[0], self.A[1],
                              self.B[0], self.B[1],
                              self.C[0], self.C[1],
                              fill='blue', outline='black')

def load_triangles_from_file(file_path):
    triangles = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 6:
                    A = (float(row[0]), float(row[1]))
                    B = (float(row[2]), float(row[3]))
                    C = (float(row[4]), float(row[5]))
                    triangles.append(Triangle(A, B, C))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить треугольники: {e}")
    return triangles

class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Треугольники")
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        load_button = tk.Button(root, text="Загрузить треугольники", command=self.load_triangles)
        load_button.pack()

        self.triangles = []

    def load_triangles(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.triangles = load_triangles_from_file(file_path)
            self.redraw_canvas()

    def redraw_canvas(self):
        self.canvas.delete('all')  # Очистить канвас
        for triangle in self.triangles:
            triangle.draw(self.canvas)

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()