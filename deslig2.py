import tkinter as tk
import threading
import subprocess

def desligar_em_5min():
    subprocess.run(["shutdown", "/s", "/t", "300"])  
    atualizar_cronometro()

def desativar_desligamento():
    subprocess.run(["shutdown", "/a"])  
    reiniciar_cronometro()

def sair():
    root.destroy()

def atualizar_cronometro():
    global tempo_restante
    tempo_restante = 300  
    cronometro_label.config(text=formatar_tempo(tempo_restante))
    atualizar_cronometro_contagem()

def reiniciar_cronometro():
    global tempo_restante
    tempo_restante = 0
    cronometro_label.config(text=formatar_tempo(tempo_restante))

def atualizar_cronometro_contagem():
    global tempo_restante
    if tempo_restante > 0:
        cronometro_label.config(text=formatar_tempo(tempo_restante))
        tempo_restante -= 1
        root.after(1000, atualizar_cronometro_contagem)
    else:
        cronometro_label.config(text="Tempo esgotado!")

def formatar_tempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    return f"{minutos:02d}:{segundos:02d}"

# Configurando a interface gráfica
root = tk.Tk()
root.title("Programa de Desligamento Automático")

# Definindo o tamanho da janela (largura x altura + margem_esquerda + margem_superior)
root.geometry("400x250+300+150")

# Botões
btn_desligar = tk.Button(root, text="Desligar em 5 min", command=desligar_em_5min)
btn_desligar.pack(pady=10)

btn_desativar = tk.Button(root, text="Desativar Desligamento", command=desativar_desligamento)
btn_desativar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

# Cronômetro
cronometro_label = tk.Label(root, text="00:00", font=("Helvetica", 16))
cronometro_label.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
