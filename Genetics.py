import random

def fitness(x):
    return x ** 2


population = [random.randint(0, 31) for _ in range(6)]

for generation in range(5):
    print(f"Generation {generation+1}:")
    print("Population:", population)

    scores = [fitness(x) for x in population]
    print("Fitness:", scores)
    parents = sorted(zip(scores, population), reverse=True)[:2]
    parent1, parent2 = parents[0][1], parents[1][1]
    print("Selected Parents:", parent1, parent2)

    crossover_point = 2
    child1 = ((parent1 >> (crossover_point + 1)) << (crossover_point + 1)) | (parent2 & ((1 << (crossover_point + 1)) - 1))
    child2 = ((parent2 >> (crossover_point + 1)) << (crossover_point + 1)) | (parent1 & ((1 << (crossover_point + 1)) - 1))
    print("Children before mutation:", child1, child2)

    if random.random() < 0.3:
        child1 ^= 1 << random.randint(0, 4)
    if random.random() < 0.3:
        child2 ^= 1 << random.randint(0, 4)
    print("Children after mutation:", child1, child2)
    population = [parent1, parent2, child1, child2]
    while len(population) < 6:
        population.append(random.randint(0, 31))    
    print()
best = max(population, key=fitness)
print("Best solution:", best)
print("Best fitness:", fitness(best))
