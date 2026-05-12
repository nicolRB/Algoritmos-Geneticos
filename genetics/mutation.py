import random

def mutate(chromosome, mutation_rate):

    for i in range(len(chromosome.genes)):

        if random.random() < mutation_rate:

            chromosome.genes[i] = 1 - chromosome.genes[i]