import tkinter as tk

# Função para adicionar números na tela
def clicar(valor):
    visor.insert(tk.END, valor)

# Função para limpar
def limpar():
    visor.delete(0, tk.END)

# Função para calcular
def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, resultado)
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x450")
janela.configure(bg="#1c1c1c")

# Visor
visor = tk.Entry(
    janela,
    font=("Arial", 28),
    bg="#1c1c1c",
    fg="white",
    justify="right",
    borderwidth=0
)
visor.pack(fill="both", padx=10, pady=20)

# Frame dos botões
frame = tk.Frame(janela, bg="#1c1c1c")
frame.pack()

botoes = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]
]

for linha in botoes:
    linha_frame = tk.Frame(frame, bg="#1c1c1c")
    linha_frame.pack()

    for botao in linha:
        if botao == "=":
            comando = calcular
            cor = "#ff9500"
        else:
            comando = lambda v=botao: clicar(v)
            cor = "#333333"

        tk.Button(
            linha_frame,
            text=botao,
            width=5,
            height=2,
            font=("Arial",20),
            bg=cor,
            fg="white",
            command=comando
        ).pack(side="left", padx=5, pady=5)

# Botão limpar
tk.Button(
    janela,
    text="C",
    font=("Arial",18),
    bg="#a5a5a5",
    command=limpar
).pack(fill="both", padx=10, pady=10)

janela.mainloop()