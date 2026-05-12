from data.items import ITEMS
from genetics.genetic_algorithm import GeneticAlgorithm

ga = GeneticAlgorithm(
    items=ITEMS,
    population_size=10,
    generations=20,
    mutation_rate=0.05,
    elite_size=1
)

best = ga.run()

print("\nMELHOR SOLUÇÃO FINAL")
print(best)