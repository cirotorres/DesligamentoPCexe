import tkinter as tk
import subprocess

def desligar_em_15min():
    subprocess.run(["shutdown", "/s", "/t", "900"])  
    atualizar_cronometro15()

def desligar_em_30min():
    subprocess.run(["shutdown", "/s", "/t", "1800"])  
    atualizar_cronometro30()

def desligar_em_60min():
    subprocess.run(["shutdown", "/s", "/t", "3600"])  
    atualizar_cronometro60()

def desligar_em_tempo():
    tempo_digitado = int(entry_tempo.get()) * 60  # Converter minutos para segundos
    subprocess.run(["shutdown", "/s", "/t", str(tempo_digitado)])  # Desliga após o tempo especificado
    atualizar_cronometro()    

def desativar_desligamento():
    subprocess.run(["shutdown", "/a"])  
    reiniciar_cronometro()

def sair():
    root.destroy()

def atualizar_cronometro15():
    global tempo_restante
    tempo_restante = 900  
    cronometro_label.config(text=formatar_tempo(tempo_restante))
    atualizar_cronometro_contagem()

def atualizar_cronometro30():
    global tempo_restante
    tempo_restante = 1800  
    cronometro_label.config(text=formatar_tempo(tempo_restante))
    atualizar_cronometro_contagem()

def atualizar_cronometro60():
    global tempo_restante
    tempo_restante = 3600  
    cronometro_label.config(text=formatar_tempo(tempo_restante))
    atualizar_cronometro_contagem()

def atualizar_cronometro():
    global tempo_restante
    tempo_restante = int(entry_tempo.get()) * 60
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
root.geometry("400x450+300+150")

label_tempo = tk.Label(root, text="Digite o tempo de desligamento (minutos):")
label_tempo.pack(pady=10)

entry_tempo = tk.Entry(root)
entry_tempo.pack(pady=5)

# Botão para desligar em tempo especificado
btn_desligar = tk.Button(root, text="Desligar em tempo especificado", command=desligar_em_tempo)
btn_desligar.pack(pady=10)

# Botões
btn_desligar = tk.Button(root, text="Desligar em 15 min", command=desligar_em_15min)
btn_desligar.pack(pady=10)
btn_desligar = tk.Button(root, text="Desligar em 30 min", command=desligar_em_30min)
btn_desligar.pack(pady=10)
btn_desligar = tk.Button(root, text="Desligar em 1 hora", command=desligar_em_60min)
btn_desligar.pack(pady=10)

btn_desativar = tk.Button(root, text="Desativar Desligamento", command=desativar_desligamento)
btn_desativar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

# Cronômetro
cronometro_label = tk.Label(root, text="00:00", font=("Helvetica", 16))
cronometro_label.pack(pady=10)


root.mainloop()
