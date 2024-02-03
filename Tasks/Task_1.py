#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Ошибка", "Неизвестная операция")
            return

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def clear_entries():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Результат:")

# Создание главного окна
root = tk.Tk()
root.title("Простой калькулятор")

# Переменные для хранения чисел и операции
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
result_label = tk.Label(root, text="Результат:")

# Создание кнопок
button_add = tk.Button(root, text="+", command=lambda: calculate('+'))
button_subtract = tk.Button(root, text="-", command=lambda: calculate('-'))
button_multiply = tk.Button(root, text="*", command=lambda: calculate('*'))
button_divide = tk.Button(root, text="/", command=lambda: calculate('/'))
button_clear = tk.Button(root, text="Сброс", command=clear_entries)

# Размещение виджетов на экране
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=1)
button_add.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=2, column=0)
button_divide.grid(row=2, column=1)
button_clear.grid(row=3, column=0)
result_label.grid(row=4, columnspan=2)

# Запуск главного цикла
root.mainloop()
