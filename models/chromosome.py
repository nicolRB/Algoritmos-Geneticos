class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
        self.total_weight = 0
        self.total_score = 0

    def __repr__(self):
        return (
            f"Genes={self.genes} | "
            f"Fitness={self.fitness} | "
            f"Peso={self.total_weight} | "
            f"Pontos={self.total_score}"
        )