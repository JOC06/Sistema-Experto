# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:56:38 2024

@author: Dell
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Diagnóstico de mantenimiento
def diagnosticar_mantenimiento():
    modelo = entry_modelo.get().lower()
    tipo = entry_tipo.get().lower()
    try:
        kilometraje = float(entry_kilometraje.get())
        consumo_gasolina = float(entry_consumo.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos para el kilometraje y consumo.")
        return
    
    conn = sqlite3.connect('vehiculos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehiculos WHERE modelo = ?", (modelo,))
    info_modelo = cursor.fetchone()
    conn.close()
    
    if info_modelo:
        _, tipo_db, kilometraje_max, consumo_gasolina_max, mantenimiento = info_modelo
        if tipo == tipo_db and kilometraje >= kilometraje_max and consumo_gasolina > consumo_gasolina_max:
            resultado = f"El vehículo modelo {modelo} necesita mantenimiento {mantenimiento}."
        else:
            resultado = "No se encontraron recomendaciones de mantenimiento para el vehículo."
    else:
        resultado = "No se encontraron datos para ese modelo de vehículo en la base de conocimientos."
    
    label_resultado.config(text=resultado)

# Configuración de la interfaz de usuario
root = tk.Tk()
root.title("AT SERVICE - Diagnóstico de Mantenimiento Vehicular")

tk.Label(root, text="Modelo del vehículo:").pack()
entry_modelo = tk.Entry(root)
entry_modelo.pack()

tk.Label(root, text="Tipo del vehículo (sedan, camioneta, etc.):").pack()
entry_tipo = tk.Entry(root)
entry_tipo.pack()

tk.Label(root, text="Kilometraje actual del vehículo:").pack()
entry_kilometraje = tk.Entry(root)
entry_kilometraje.pack()

tk.Label(root, text="Consumo de gasolina promedio (km/l):").pack()
entry_consumo = tk.Entry(root)
entry_consumo.pack()

btn_diagnosticar = tk.Button(root, text="Diagnosticar", command=diagnosticar_mantenimiento)
btn_diagnosticar.pack()

label_resultado = tk.Label(root, text="", wraplength=400, justify="left")
label_resultado.pack(pady=10)

root.mainloop()