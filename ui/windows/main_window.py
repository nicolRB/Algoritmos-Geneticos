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

        # Melhor indivíduo
        self.best_label = ctk.CTkLabel(
            self,
            text="Nenhuma população iniciada",
            font=("Arial", 16),
            justify="left"
        )

        self.best_label.pack(pady=20)

    def initialize_population(self):

        self.ga.initialize_population()

        best = self.ga.get_best()

        self.update_best_display(best)

    def next_generation(self):

        # caso haja uma população, evolui para a próxima geração
        if not self.ga.population:
            CTkMessagebox(
                title="Erro",
                message="Nenhuma população iniciada. Inicie a população primeiro."
            )
            return
        else:
            best = self.ga.next_generation()

            self.generation_label.configure(
                text=f"Geração: {self.ga.current_generation}"
            )

            self.update_best_display(best)

    def update_best_display(self, chromosome):

        text = (
            f"Genes: {chromosome.genes}\n"
            f"Fitness: {chromosome.fitness}\n"
            f"Peso: {chromosome.total_weight}\n"
            f"Pontos: {chromosome.total_score}"
        )

        self.best_label.configure(text=text)

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