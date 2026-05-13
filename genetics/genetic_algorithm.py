from genetics.population import create_population
from genetics.evolution import evolve_population

class GeneticAlgorithm:

    def __init__(
        self,
        items,
        population_size,
        generations,
        mutation_rate,
        elite_size=1
    ):

        self.items = items

        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size

        self.population = []

        self.best_history = []
        self.average_history = []

        self.best_chromosome = None

    def run(self):

        # População inicial
        self.population = create_population(
            self.population_size,
            self.items
        )

        # Evolução
        for generation in range(self.generations):

            self.population = evolve_population(
                self.population,
                self.items,
                self.mutation_rate,
                self.elite_size
            )

            # Melhor indivíduo
            best = max(
                self.population,
                key=lambda chromosome: chromosome.fitness
            )

            # Média fitness
            average = (
                sum(c.fitness for c in self.population)
                / len(self.population)
            )

            # Histórico
            self.best_history.append(best.fitness)
            self.average_history.append(average)

            # Melhor global
            if (
                self.best_chromosome is None or
                best.fitness > self.best_chromosome.fitness
            ):
                self.best_chromosome = best.copy()

            # Debug
            print(f"\nGERAÇÃO {generation + 1}")
            print(best)

        return self.best_chromosome
    
    def initialize_population(self):

        self.population = create_population(
            self.population_size,
            self.items
        )

        self.current_generation = 0

        self.best_history = []
        self.average_history = []

        self.best_chromosome = None

        best = max(
            self.population,
            key=lambda c: c.fitness
        )

        average = (
            sum(c.fitness for c in self.population)
            / len(self.population)
        )

        self.best_history.append(best.fitness)
        self.average_history.append(average)

        self.best_chromosome = best.copy()

        return self.population

    def next_generation(self):

        self.population = evolve_population(
            self.population,
            self.items,
            self.mutation_rate,
            self.elite_size
        )

        self.current_generation += 1

        best = max(
            self.population,
            key=lambda c: c.fitness
        )

        average = (
            sum(c.fitness for c in self.population)
            / len(self.population)
        )

        self.best_history.append(best.fitness)
        self.average_history.append(average)

        if (
            self.best_chromosome is None or
            best.fitness > self.best_chromosome.fitness
        ):
            self.best_chromosome = best.copy()

        return best
    
    def get_best(self):

        if not self.population:
            return None

        return max(self.population, key=lambda c: c.fitness)