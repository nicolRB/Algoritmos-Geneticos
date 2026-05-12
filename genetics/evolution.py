from genetics.selection import tournament_selection
from genetics.crossover import single_point_crossover
from genetics.mutation import mutate
from genetics.fitness import calculate_fitness

def evolve_population(
    population,
    items,
    mutation_rate,
    elite_size=1
):

    # Ordena do melhor para o pior
    sorted_population = sorted(
        population,
        key=lambda chromosome: chromosome.fitness,
        reverse=True
    )

    new_population = []

    # Elitismo
    for i in range(elite_size):
        elite = sorted_population[i].copy()
        new_population.append(elite)

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

        # Recalcula fitness
        calculate_fitness(child1, items)
        calculate_fitness(child2, items)

        # Apenas filhos válidos
        if child1.total_weight <= 30:
            new_population.append(child1)

        if (
            child2.total_weight <= 30 and
            len(new_population) < population_size
        ):
            new_population.append(child2)

    return new_population