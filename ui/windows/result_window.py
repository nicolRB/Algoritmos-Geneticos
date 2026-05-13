import customtkinter as ctk


class ResultWindow(ctk.CTkToplevel):

    def __init__(self, parent, chromosome):

        super().__init__(parent)

        self.title("Resultado Final")

        self.geometry("400x300")

        text = (
            f"Melhor Cromossomo\n\n"
            f"Genes: {chromosome.genes}\n"
            f"Fitness: {chromosome.fitness}\n"
            f"Peso: {chromosome.total_weight}\n"
            f"Pontos: {chromosome.total_score}"
        )

        self.label = ctk.CTkLabel(
            self,
            text=text,
            font=("Arial", 16)
        )

        self.label.pack(pady=30)