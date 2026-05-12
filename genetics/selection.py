import random

def tournament_selection(population, tournament_size=3):

    tournament = random.sample(population, tournament_size)

    best = max(tournament, key=lambda chromosome: chromosome.fitness)

    return best