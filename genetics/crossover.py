import random

from models.chromosome import Chromosome

def single_point_crossover(parent1, parent2):

    size = len(parent1.genes)

    crossover_point = random.randint(1, size - 1)

    child1_genes = (
        parent1.genes[:crossover_point] +
        parent2.genes[crossover_point:]
    )

    child2_genes = (
        parent2.genes[:crossover_point] +
        parent1.genes[crossover_point:]
    )

    child1 = Chromosome(child1_genes)
    child2 = Chromosome(child2_genes)

    return child1, child2