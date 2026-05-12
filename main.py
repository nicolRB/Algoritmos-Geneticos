from data.items import ITEMS
from genetics.population import create_population

POPULATION_SIZE = 10

population = create_population(POPULATION_SIZE, ITEMS)

print("POPULAÇÃO INICIAL\n")

for index, chromosome in enumerate(population):

    print(f"Indivíduo {index + 1}")
    print(chromosome)
    print()