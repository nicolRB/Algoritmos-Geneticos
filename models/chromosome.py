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
    
    def copy(self):
        clone = Chromosome(self.genes.copy())

        clone.fitness = self.fitness
        clone.total_weight = self.total_weight
        clone.total_score = self.total_score

        return clone