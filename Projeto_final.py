import json
import tkinter as tk
from tkinter import messagebox, simpledialog

print("Olá! Bem Vindo")

class RegistroDeFaltas:
    def __init__(self):
        self.faltas = {}

    def adicionar_falta(self, nome, motivo):
        if nome not in self.faltas:
            self.faltas[nome] = []
        self.faltas[nome].append(motivo)
        messagebox.showinfo("Sucesso", f"Falta registrada para {nome}: {motivo}")

    def visualizar_faltas(self):
        if not self.faltas:
            messagebox.showinfo("Visualizar Faltas", "Nenhuma falta registrada.")
            return
        resultado = ""
        for nome, motivos in self.faltas.items():
            resultado += f"\n{nome}:\n"
            for i, motivo in enumerate(motivos, start=1):
                resultado += f"  {i}. {motivo}\n"
        messagebox.showinfo("Registro de Faltas", resultado)

    def contar_faltas(self):
        if not self.faltas:
            messagebox.showinfo("Contar Faltas", "Nenhuma falta registrada.")
            return
        resultado = "Quantidade de Faltas por Aluno:\n"
        for nome, motivos in self.faltas.items():
            resultado += f"{nome}: {len(motivos)} falta(s)\n"
        messagebox.showinfo("Contar Faltas", resultado)

    def remover_falta(self, nome, indice):
        if nome in self.faltas and 0 < indice <= len(self.faltas[nome]):
            removido = self.faltas[nome].pop(indice - 1)
            messagebox.showinfo("Sucesso", f"Falta removida para {nome}: {removido}")
            if not self.faltas[nome]:
                del self.faltas[nome]
        else:
            messagebox.showerror("Erro", f"Índice inválido ou aluno {nome} não encontrado.")

    def salvar_registros(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump(self.faltas, f)
        messagebox.showinfo("Sucesso", "Registros salvos com sucesso.")

    def carregar_registros(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.faltas = json.load(f)
            messagebox.showinfo("Sucesso", "Registros carregados com sucesso.")
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "Arquivo não encontrado. Iniciando com registros vazios.")

def adicionar_falta_interface():
    nome = simpledialog.askstring("Adicionar Falta", "Nome do aluno:")
    motivo = simpledialog.askstring("Adicionar Falta", "Motivo da falta:")
    if nome and motivo:
        registrador.adicionar_falta(nome, motivo)

def remover_falta_interface():
    nome = simpledialog.askstring("Remover Falta", "Nome do aluno:")
    indice = simpledialog.askinteger("Remover Falta", "Número da falta a ser removida:")
    if nome and indice:
        registrador.remover_falta(nome, indice)

def main():
    global registrador
    registrador = RegistroDeFaltas()
    arquivo = 'registros_de_faltas.json'
    
    root = tk.Tk()
    root.title("Registro de Faltas")

    tk.Button(root, text="Adicionar Falta", command=adicionar_falta_interface).pack(pady=10)
    tk.Button(root, text="Visualizar Faltas", command=registrador.visualizar_faltas).pack(pady=10)
    tk.Button(root, text="Contar Faltas", command=registrador.contar_faltas).pack(pady=10)
    tk.Button(root, text="Remover Falta", command=remover_falta_interface).pack(pady=10)
    tk.Button(root, text="Salvar Registros", command=lambda: registrador.salvar_registros(arquivo)).pack(pady=10)
    tk.Button(root, text="Carregar Registros", command=lambda: registrador.carregar_registros(arquivo)).pack(pady=10)
    tk.Button(root, text="Sair", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()