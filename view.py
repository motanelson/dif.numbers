
import tkinter as tk
from tkinter import filedialog

def carregar_ficheiro():
    filename = filedialog.askopenfilename(
        title="Escolher ficheiro TXT",
        filetypes=[("Ficheiros de texto", "*.txt")]
    )
    if not filename:
        return

    with open(filename, "r") as f:
        conteudo = f.read().strip()

    try:
        dados = list(map(int, conteudo.split(",")))
    except ValueError:
        print("Erro: ficheiro inválido, não contém apenas inteiros separados por vírgulas.")
        return

    if not dados:
        return

    dados.sort()
    minimo = min(dados)
    maximo = max(dados)
    diferenca = maximo - minimo if maximo != minimo else 1

    escala_y = ALTURA / diferenca
    escala_x = LARGURA / len(dados)

    canvas.delete("all")

    # grelha horizontal
    for y in range(0, ALTURA, 20):
        canvas.create_line(0, y, LARGURA, y, fill="lightgray")
        valor = maximo - int(y / escala_y)
        canvas.create_text(5, y, text=str(valor), anchor="w", fill="black")

    # pontos
    for i, valor in enumerate(dados):
        x = i * escala_x
        y = ALTURA - (valor - minimo) * escala_y
        canvas.create_oval(x, y, x+2, y+2, fill="black", outline="black")

# dimensões
LARGURA = 800
ALTURA = 600

root = tk.Tk()
root.title("Plot de dados TXT")
root.geometry(f"{LARGURA}x{ALTURA}")

# dividir em duas áreas: canvas (em cima) + barra (em baixo)
canvas = tk.Canvas(root, width=LARGURA, height=ALTURA-40, bg="yellow")
canvas.pack(side="top", fill="both", expand=True)

frame_botoes = tk.Frame(root, bg="yellow", height=40)
frame_botoes.pack(side="bottom", fill="x")

btn = tk.Button(frame_botoes, text="Carregar ficheiro .txt", command=carregar_ficheiro)
btn.pack(pady=5)

root.mainloop()
