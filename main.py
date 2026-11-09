import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")

titulo = tk.Label(window, text="Minha agenda", font = ("Arial", 14, "bold")).pack(pady=20) 

#Entrada dos Dados do Compromisso
entrada = tk.Entry(window, width=30)
entrada.pack(pady=(10))
entrada.insert(0, "Digite o Compromisso")

window.geometry("900x600")

window.mainloop()