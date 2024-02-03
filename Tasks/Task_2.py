#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

# Функция, вызываемая при нажатии на кнопку
def set_color(color_name, color_code):
    # Обновляем текстовое поле и метку
    entry_color_code.delete(0, tk.END)  # Очищаем текстовое поле перед вставкой
    entry_color_code.insert(0, color_code)  # Вставляем код цвета в текстовое поле
    label_color_name.config(text=color_name)  # Обновляем текст метки

# Создание основного окна приложения
root = tk.Tk()
root.title("Цвета радуги")

# Словарь с названиями и кодами цветов
colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff",
}

# Создание метки и текстового поля для отображения выбранного цвета
label_color_name = tk.Label(root, text="Название цвета", font=("Arial", 12))
label_color_name.pack(pady=5)

entry_color_code = tk.Entry(root, font=("Arial", 12))
entry_color_code.pack(pady=5)

# Создание кнопок для каждого цвета радуги
for color_name, color_code in colors.items():
    button = tk.Button(root, text=color_name, bg=color_code, fg="white",
                       command=lambda name=color_name, code=color_code: set_color(name, code))
    button.pack(pady=2)

# Запуск главного цикла Tkinter
root.mainloop()
