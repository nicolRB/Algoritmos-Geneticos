import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from data.items import ITEMS
from genetics.genetic_algorithm import GeneticAlgorithm

import ui.windows.result_window as result_window


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        # Janela
        self.title("Algoritmo Genético - Mochila")

        self.geometry("1000x700")

        # Algoritmo
        self.ga = GeneticAlgorithm(
            items=ITEMS,
            population_size=10,
            generations=20,
            mutation_rate=0.05,
            elite_size=1
        )

        # UI
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = ctk.CTkLabel(
            self,
            text="Problema da Mochila",
            font=("Arial", 28)
        )

        self.title_label.pack(pady=20)

        # Botão iniciar
        self.start_button = ctk.CTkButton(
            self,
            text="Iniciar População",
            command=self.initialize_population
        )

        self.start_button.pack(pady=10)

        # Botão próxima geração
        self.next_button = ctk.CTkButton(
            self,
            text="Próxima Geração",
            command=self.next_generation
        )

        self.next_button.pack(pady=10)

        # Botão resultado final (cria a janela de resultado)
        self.result_button = ctk.CTkButton(
            self,
            text="Resultado Final",
            command=self.show_result
        )

        self.result_button.pack(pady=10)

        # Label geração
        self.generation_label = ctk.CTkLabel(
            self,
            text="Geração: 0",
            font=("Arial", 18)
        )

        self.generation_label.pack(pady=10)
        
        # Frame da tabela
        self.table_frame = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=400
        )

        headers = ["ID", "Genes", "Fitness", "Peso", "Pontos"]

        for col in range(len(headers)):
            self.table_frame.grid_columnconfigure(col, weight=1)

        for col, text in enumerate(headers):

            self.table_frame.grid_columnconfigure(col, weight=1)

            header_cell = ctk.CTkFrame(
                self.table_frame,
                fg_color="#1F1F1F",
                corner_radius=0,
                border_width=1,
                border_color="#555555"
            )

            header_cell.grid(
                row=0,
                column=col,
                padx=1,
                pady=1,
                sticky="nsew"
            )

            label = ctk.CTkLabel(
                header_cell,
                text=text,
                font=("Arial", 16, "bold"),
                anchor="center"
            )

            label.pack(
                padx=20,
                pady=12,
                fill="both",
                expand=True
            )

        self.table_frame.pack(pady=20, fill="both", expand=True)

    def initialize_population(self):

        self.ga.initialize_population()

        self.update_population_table()

    def next_generation(self):

        # caso haja uma população, evolui para a próxima geração
        if not self.ga.population:
            CTkMessagebox(
                title="Erro",
                message="Nenhuma população iniciada. Inicie a população primeiro."
            )
            return
        else:
            self.ga.next_generation()

            self.generation_label.configure(
                text=f"Geração: {self.ga.current_generation}"
            )

            self.update_population_table()

    def show_result(self):
        if not self.ga.population:
            CTkMessagebox(
                title="Erro",
                message="Nenhuma população iniciada. Inicie a população primeiro."
            )
            return

        best = self.ga.get_best()

        #abre a janela de resultado final com os dados do melhor cromossomo encontrado e move a janela para frente
        result_window.ResultWindow(self, best)

    def update_population_table(self):

        # Remove linhas antigas
        for widget in self.table_frame.winfo_children():

            info = widget.grid_info()

            if info["row"] != 0:
                widget.destroy()

        # Cria linhas da população
        for row, chromosome in enumerate(self.ga.population, start=1):

            values = [
                row - 1,
                str(chromosome.genes),
                chromosome.fitness,
                chromosome.total_weight,
                chromosome.total_score
            ]

            for col, value in enumerate(values):

                cell = ctk.CTkFrame(
                    self.table_frame,
                    fg_color="#2B2B2B",
                    corner_radius=0,
                    border_width=1,
                    border_color="#444444"
                )

                cell.grid(
                    row=row,
                    column=col,
                    padx=1,
                    pady=1,
                    sticky="nsew"
                )

                label = ctk.CTkLabel(
                    cell,
                    text=str(value),
                    font=("Arial", 14),
                    anchor="center"
                )

                label.pack(
                    padx=20,
                    pady=10,
                    fill="both",
                    expand=True
                )