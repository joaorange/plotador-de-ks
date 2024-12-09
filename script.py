import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

# Lendo o CSV
def read_csv(file_path, sep, decimal='.'):
    return pd.read_csv(file_path, sep=sep, decimal=decimal)

# Transformando a coluna "target" em valores de "1" e "0"
def event_nonevent(df, event_column, event_value, non_event_value):
    df = df.copy()
    df[event_column] = df[event_column].apply(lambda x: 1 if x == event_value else (0 if x == non_event_value else x))
    return df

# Gráfico para visualização da curva de KS
def graph_ks(df, event_column, probability_column, event_value, non_event_value):
    score_0 = df[df[event_column] == 0][probability_column]
    score_1 = df[df[event_column] == 1][probability_column]

    x_0 = np.sort(score_0)
    y_0 = np.arange(1, len(x_0) + 1) / len(x_0)

    x_1 = np.sort(score_1)
    y_1 = np.arange(1, len(x_1) + 1) / len(x_1)

    x_all = np.sort(np.concatenate((x_0, x_1)))
    y_0_interp = np.searchsorted(x_0, x_all, side='right') / len(x_0)
    y_1_interp = np.searchsorted(x_1, x_all, side='right') / len(x_1)
    difference = np.abs(y_0_interp - y_1_interp)

    ks_statistic = np.max(difference)
    ks_index = np.argmax(difference)
    ks_x_value = x_all[ks_index]
    ks_y_value = y_0_interp[ks_index]

    plt.figure(figsize=(10, 6))
    plt.plot(x_0, y_0, marker='o', label=non_event_value, linestyle='-', color='blue')
    plt.plot(x_1, y_1, marker='o', label=event_value, linestyle='-', color='orange')

    plt.annotate(f'KS = {ks_statistic:.2f}', xy=(ks_x_value, ks_y_value),
                 xytext=(ks_x_value + 0.1, ks_y_value - 0.1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.title('Distribuição Acumulada dos Scores por Classe com KS')
    plt.xlabel('SCORE')
    plt.ylabel('Fração Acumulada')
    plt.legend()
    plt.grid()
    plt.show()

# Processando o CSV com base nas entradas do tkinter
def process_csv(sep_entry, decimal_entry, event_column_entry, probability_column_entry, event_value_entry, non_event_value_entry):
    file_path = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    sep = sep_entry.get()
    decimal = decimal_entry.get() if decimal_entry.get() else '.'
    event_column = event_column_entry.get()
    probability_column = probability_column_entry.get()
    event_value = event_value_entry.get()
    non_event_value = non_event_value_entry.get()

    try:
        df = read_csv(file_path, sep, decimal)
        df = event_nonevent(df, event_column, event_value, non_event_value)
        graph_ks(df, event_column, probability_column, event_value, non_event_value)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Criando o software
def create_gui():
    root = tk.Tk()
    root.title("Análise KS")

    tk.Label(root, text="Separador do CSV (por exemplo, ';'):").grid(row=0, column=0)
    sep_entry = tk.Entry(root)
    sep_entry.grid(row=0, column=1)

    tk.Label(root, text="Decimal, se houver (o default é '.'):").grid(row=1, column=0)
    decimal_entry = tk.Entry(root)
    decimal_entry.grid(row=1, column=1)

    tk.Label(root, text="Coluna de Evento:").grid(row=2, column=0)
    event_column_entry = tk.Entry(root)
    event_column_entry.grid(row=2, column=1)

    tk.Label(root, text="Coluna de Probabilidade:").grid(row=3, column=0)
    probability_column_entry = tk.Entry(root)
    probability_column_entry.grid(row=3, column=1)

    tk.Label(root, text="Valor do Evento:").grid(row=4, column=0)
    event_value_entry = tk.Entry(root)
    event_value_entry.grid(row=4, column=1)

    tk.Label(root, text="Valor do Não Evento:").grid(row=5, column=0)
    non_event_value_entry = tk.Entry(root)
    non_event_value_entry.grid(row=5, column=1)

    tk.Button(root, text="Selecionar CSV e Gerar Gráfico", command=lambda: process_csv(
        sep_entry, decimal_entry, event_column_entry, probability_column_entry, event_value_entry, non_event_value_entry
    )).grid(row=6, columnspan=2)

    root.mainloop()

def main():
    create_gui()

if __name__ == "__main__":
    main()
