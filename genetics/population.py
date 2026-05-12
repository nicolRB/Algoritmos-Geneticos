import random

from models.chromosome import Chromosome
from utils.constants import CHROMOSOME_SIZE
from genetics.fitness import calculate_fitness

def create_random_chromosome(items):

    while True:

        genes = []

        for _ in range(CHROMOSOME_SIZE):
            genes.append(random.randint(0, 1))

        chromosome = Chromosome(genes)

        calculate_fitness(chromosome, items)

        # Apenas indivíduos válidos
        if chromosome.total_weight <= 30:
            return chromosome


def create_population(size, items):

    population = []

    for _ in range(size):
        chromosome = create_random_chromosome(items)
        population.append(chromosome)

    return population