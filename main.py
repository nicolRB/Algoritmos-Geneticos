from data.items import ITEMS
from genetics.population import create_population
from genetics.evolution import evolve_population

POPULATION_SIZE = 10
GENERATIONS = 5
MUTATION_RATE = 0.05

population = create_population(POPULATION_SIZE, ITEMS)

print("POPULAÇÃO INICIAL\n")

for index, chromosome in enumerate(population):

    print(f"Indivíduo {index + 1}")
    print(chromosome)
    print()

for generation in range(GENERATIONS):

    population = evolve_population(
        population,
        ITEMS,
        MUTATION_RATE
    )

    best = max(population, key=lambda chromosome: chromosome.fitness)

    print(f"\nGERAÇÃO {generation + 1}")
    print(best)