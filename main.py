import tkinter as tk
from geral import PesquisaGeral

def obter_dados():
    numeros_nf = entrada_dados_texto.get("1.0", tk.END).split()
    cnpj = entrada_dados_numero.get()

    if len(cnpj) < 14:
        print("CNPJ inválido!")
        return
    
    root.destroy()
    PesquisaGeral.abrir_progresso(cnpj, numeros_nf)

def validar_entrada(text):
    return text.isdigit() and len(text) <= 14

def limitar_caracteres(event):
    linha_atual, coluna_atual = map(int, entrada_dados_texto.index(tk.INSERT).split('.'))
    texto_linha_atual = entrada_dados_texto.get(f"{linha_atual}.0", f"{linha_atual}.end")
    if len(texto_linha_atual) >= 6 and event.keysym != "BackSpace":
        entrada_dados_texto.insert(f"{linha_atual}.{coluna_atual}", "\n")
        return 'break'
    
root = tk.Tk()
root.geometry("1225x710")
root.resizable(False, False)
root.title("Coleta de Informações SBC")

# Fundo da imagem
fundoImg = tk.PhotoImage(file="Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Robert/BannerWEN.PNG")
label1 = tk.Label(root, image=fundoImg)
label1.place(x = 0,y = 0)

# Texto explicativo para o CNPJ
texto_explicativo_numero = tk.Label(root, text="Insira o CNPJ:", font=('calibri', 20, 'bold'))
texto_explicativo_numero.grid(column=0, row=1, padx=400, pady=20)

# Entrada para o CNPJ
validacao = root.register(validar_entrada)
entrada_dados_numero = tk.Entry(root, validate="key", validatecommand=(validacao, "%P"), width=20, font=('calibri', 20, 'bold'))
entrada_dados_numero.grid(column=0, row=2, padx=400, pady=10)

# Texto explicativo para os números de documento
texto_explicativo_texto = tk.Label(root, text="Insira todos os números de documento:", font=('calibri', 20, 'bold'))
texto_explicativo_texto.grid(column=0, row=3, padx=400, pady=20)

# Entrada de texto para os números de documento
entrada_dados_texto = tk.Text(root, height=10, width=15, font=('calibri', 20, 'bold'))
entrada_dados_texto.bind("<Key>", limitar_caracteres)
entrada_dados_texto.grid(column=0, row=4, padx=400, pady=10)

# Botão de envio
botao_enviar = tk.Button(root, text="Iniciar Busca", command=obter_dados, font=('calibri', 20, 'bold'))
botao_enviar.grid(column=0, row=5, padx=400, pady=20)

root.mainloop()
