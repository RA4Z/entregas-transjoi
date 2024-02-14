import tkinter as tk
from tkinter import ttk
import datetime

class ProgressBar:
    def __init__(self, progress, root, info_atual):
        self.progress = progress
        self.info_atual = info_atual
        self.root = root
        self.progress['value'] = 0

    def incrementar_progresso(self, index, total):
        value = (index / total) * 100
        self.progress['value'] = value
        self.info_atual['text'] = "Foram pesquisadas {} de {}".format(index, total)
        self.root.update()
    
    def fechar_sistema(self):
        self.root.destroy()

class PesquisaGeral:
    def __init__(self, cnpj, todos_nf, progress_bar):
        self.cnpj = cnpj
        self.todos_nf = todos_nf
        self.progress_bar = progress_bar

    def pesquisar_web(self):
        from navegador import NavegarWeb
        current_time = datetime.datetime.now()
        arquivo = '{}-cnpj{}.txt'.format(current_time.microsecond, self.cnpj)
        index = 0

        with open('hist_exec/{}'.format(arquivo), 'w') as f:
            f.write('CNPJ, Numero NF, Data Coletado, Data Entregue\n')
            for nf in self.todos_nf:
                print(nf)
                try:
                    datas = NavegarWeb.transjoi(self.cnpj, nf)
                    linha_dados = '{}, {}, {}\n'.format(self.cnpj, nf, datas)
                except:
                    linha_dados = '{}, {}, Not Found, Not Found\n'.format(self.cnpj, nf)
                f.write(linha_dados)
                index += 1
                self.progress_bar.incrementar_progresso(index, len(self.todos_nf))
                NavegarWeb.nova_consulta()
        NavegarWeb.fechar()
        self.progress_bar.fechar_sistema()

    @staticmethod
    def abrir_progresso(cnpj, todos_nf):
        root = tk.Tk()
        root.geometry("500x200")
        root.resizable(False, False)
        root.title("Buscando Entregas Transjoi...")

        progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        progresso.pack(pady=20)

        info_atual = tk.Label(root, text="Existem {} itens a serem pesquisados, pressione no botão abaixo para iniciar!".format(len(todos_nf)), )
        info_atual.pack(pady=20)
        
        barra_progresso = ProgressBar(progresso, root, info_atual)

        botao_iniciar = tk.Button(root, text="Iniciar Pesquisa", command=lambda: PesquisaGeral.pesquisar(cnpj, todos_nf, barra_progresso))
        botao_iniciar.pack()
        root.mainloop()

    @staticmethod
    def pesquisar(cnpj, todos_nf, barra_progresso):
        pesquisa = PesquisaGeral(cnpj, todos_nf, barra_progresso)
        pesquisa.pesquisar_web()

