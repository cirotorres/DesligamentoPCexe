import tkinter as tk
import subprocess

def desligar_em_30min():
    subprocess.run(["shutdown", "/s", "/t", "1800"])  

def desativar_desligamento():
    subprocess.run(["shutdown", "/a"])  

def sair():
    root.destroy()

# Configurando a interface gráfica
root = tk.Tk()
root.title("Programa de Desligamento Automático")

# Definindo o tamanho da janela (largura x altura + margem_esquerda + margem_superior)
root.geometry("400x200+300+150")

# Botões
btn_desligar = tk.Button(root, text="Desligar em 30 min", command=desligar_em_30min)
btn_desligar.pack(pady=10)

btn_desativar = tk.Button(root, text="Desativar Desligamento", command=desativar_desligamento)
btn_desativar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
