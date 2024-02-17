# ---------------------------------------
import numpy as np

# Define parameters
target_sum = 1200
array_size = 21
allowed_numbers = [30, 50, 70]

population_size = 100
mutation_rate = 0.1
generations = 1000



# Define fitness function
def fitness_function(array):
    return abs(sum(array) - target_sum)


# Initialize population
def initialize_population():
    return [np.random.choice(allowed_numbers, array_size) for _ in range(population_size)]


# Crossover
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, array_size)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


# Mutation
def mutate(child):
    for i in range(array_size):
        if np.random.random() < mutation_rate:
            child[i] = np.random.choice(allowed_numbers)
    return child


# Genetic algorithm
def genetic_algorithm():
    population = initialize_population()
    for generation in range(generations):
        # Calculate fitness for each individual
        fitness_scores = [fitness_function(individual) for individual in population]

        # Selection: choose the best individuals as parents
        sorted_indices = np.argsort(fitness_scores)
        selected_parents = [population[i] for i in sorted_indices[:population_size // 2]]

        # Reproduction: crossover and mutation
        children = []
        while len(children) < population_size - len(selected_parents):
            # Randomly select two parents without replacement
            parent_indices = np.random.permutation(len(selected_parents))[:2]
            parent1, parent2 = selected_parents[parent_indices[0]], selected_parents[parent_indices[1]]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            children.append(child1)
            children.append(child2)

        # Replace old population with new population
        population = selected_parents + children

        # Check for convergence
        if fitness_function(population[0]) == 0:
            return population[0]

    # Return the best individual found
    return population[0]




