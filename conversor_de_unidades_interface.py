import tkinter as tk
from tkinter import ttk, messagebox

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) / 1.8

def fahrenheit_para_kelvin(f):
    return fahrenheit_para_celsius(f) + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return k * (9/5) - 459.67

def converter_temperatura():
    try:
        valor = float(entrada_valor.get())
        tipo = tipo_temperatura.get()
        if tipo == "C":
            f = celsius_para_fahrenheit(valor)
            k = celsius_para_kelvin(valor)
            resultado.set(f"{valor}°C = {f:.2f}°F\n{valor}°C = {k:.2f} K")
        elif tipo == "F":
            c = fahrenheit_para_celsius(valor)
            k = fahrenheit_para_kelvin(valor)
            resultado.set(f"{valor}°F = {c:.2f}°C\n{valor}°F = {k:.2f} K")
        elif tipo == "K":
            c = kelvin_para_celsius(valor)
            f = kelvin_para_fahrenheit(valor)
            resultado.set(f"{valor} K = {c:.2f}°C\n{valor} K = {f:.2f}°F")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

def converter_distancia():
    try:
        valor = float(entrada_valor.get())
        tipo = tipo_distancia.get()
        if tipo == "Metros":
            km = valor / 1000
            cm = valor * 100
            resultado.set(f"{valor} m = {km:.2f} km\n{valor} m = {cm:.2f} cm")
        elif tipo == "Quilômetros":
            m = valor * 1000
            cm = m * 100
            resultado.set(f"{valor} km = {m:.2f} m\n{valor} km = {cm:.2f} cm")
        elif tipo == "Centímetros":
            m = valor / 100
            km = m / 1000
            resultado.set(f"{valor} cm = {m:.2f} m\n{valor} cm = {km:.2f} km")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

def converter_peso():
    try:
        valor = float(entrada_valor.get())
        tipo = tipo_peso.get()
        if tipo == "Gramas":
            kg = valor / 1000
            mg = valor * 1000
            resultado.set(f"{valor} g = {kg:.2f} kg\n{valor} g = {mg:.2f} mg")
        elif tipo == "Quilogramas":
            g = valor * 1000
            mg = g * 1000
            resultado.set(f"{valor} kg = {g:.2f} g\n{valor} kg = {mg:.2f} mg")
        elif tipo == "Miligramas":
            g = valor / 1000
            kg = g / 1000
            resultado.set(f"{valor} mg = {g:.2f} g\n{valor} mg = {kg:.2f} kg")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico.")

def escolher_conversao():
    tipo = tipo_conversao.get()
    if tipo == "Temperatura":
        frame_tipo_temperatura.grid(row=1, column=2, padx=10, pady=10)
        frame_tipo_distancia.grid_forget()
        frame_tipo_peso.grid_forget()
    elif tipo == "Distância":
        frame_tipo_distancia.grid(row=1, column=2, padx=10, pady=10)
        frame_tipo_temperatura.grid_forget()
        frame_tipo_peso.grid_forget()
    elif tipo == "Peso":
        frame_tipo_peso.grid(row=1, column=2, padx=10, pady=10)
        frame_tipo_temperatura.grid_forget()
        frame_tipo_distancia.grid_forget()

def converter():
    tipo = tipo_conversao.get()
    if tipo == "Temperatura":
        converter_temperatura()
    elif tipo == "Distância":
        converter_distancia()
    elif tipo == "Peso":
        converter_peso()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Unidades")
janela.geometry("550x250")

# Widgets da interface
label_conversao = tk.Label(janela, text="Escolha a Conversão:")
label_conversao.grid(row=0, column=0, padx=10, pady=10)

tipo_conversao = ttk.Combobox(janela, values=["Temperatura", "Distância", "Peso"])
tipo_conversao.grid(row=0, column=1, padx=10, pady=10)
tipo_conversao.bind("<<ComboboxSelected>>", lambda event: escolher_conversao())

label_valor = tk.Label(janela, text="Valor:")
label_valor.grid(row=1, column=0, padx=10, pady=10)

entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=1, column=1, padx=10, pady=10)

# Frames para os radio buttons
frame_tipo_temperatura = tk.Frame(janela)
frame_tipo_distancia = tk.Frame(janela)
frame_tipo_peso = tk.Frame(janela)

# Combobox para temperatura
tipo_temperatura = ttk.Combobox(frame_tipo_temperatura, values=["C", "F", "K"])
tipo_temperatura.pack(padx=10, pady=10)

# Combobox para distância
tipo_distancia = ttk.Combobox(frame_tipo_distancia, values=["Metros", "Quilômetros", "Centímetros"])
tipo_distancia.pack(padx=10, pady=10)

# Combobox para peso
tipo_peso = ttk.Combobox(frame_tipo_peso, values=["Gramas", "Quilogramas", "Miligramas"])
tipo_peso.pack(padx=10, pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado)
label_resultado.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Inicia a interface
janela.mainloop()
