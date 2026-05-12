MAX_WEIGHT = 30

def calculate_fitness(chromosome, items):
    total_weight = 0
    total_score = 0

    for gene, item in zip(chromosome.genes, items):
        if gene:
            total_weight += item.weight
            total_score += item.score

    if total_weight > MAX_WEIGHT:
        return 0

    return total_score