from genetics.selection import tournament_selection
from genetics.crossover import single_point_crossover
from genetics.mutation import mutate
from genetics.fitness import calculate_fitness

def evolve_population(population, items, mutation_rate):

    new_population = []

    population_size = len(population)

    while len(new_population) < population_size:

        # Seleção
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        # Crossover
        child1, child2 = single_point_crossover(parent1, parent2)

        # Mutação
        mutate(child1, mutation_rate)
        mutate(child2, mutation_rate)

        # Fitness
        calculate_fitness(child1, items)
        calculate_fitness(child2, items)

        # Validação
        if child1.total_weight <= 30:
            new_population.append(child1)

        if (
            child2.total_weight <= 30 and
            len(new_population) < population_size
        ):
            new_population.append(child2)

    return new_population