from utils.constants import MAX_WEIGHT

def calculate_fitness(chromosome, items):

    total_weight = 0
    total_score = 0

    for gene, item in zip(chromosome.genes, items):

        if gene == 1:
            total_weight += item.weight
            total_score += item.score

    chromosome.total_weight = total_weight
    chromosome.total_score = total_score

    # Penalização
    if total_weight > MAX_WEIGHT:
        chromosome.fitness = 0
    else:
        chromosome.fitness = total_score

    return chromosome.fitness