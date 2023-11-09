import random

# prompt user for board size
n = int(input("Enter board size: "))

# define the population size and number of generations
pop_size = 10
num_generations = 300

# define the fitness function
def fitness(board):
    clashes = 0
    # loop through each queen and compare it to every other queen
    for i in range(n):
        for j in range(i+1, n):
            # if the queens are in the same row or diagonal, increment clashes
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                clashes += 1
    return clashes



# define the selection function
def selection(population):
    fits = [fitness(p) for p in population]
    fits_sum = sum(fits)
    # calculate the probability of each individual being selected
    probs = [f/fits_sum for f in fits]
    cum_probs = [sum(probs[:i+1]) for i in range(len(probs))]
    new_pop = []
    # select new individuals using roulette wheel selection
    for i in range(pop_size):
        r = random.random()
        for j in range(len(cum_probs)):
            if r < cum_probs[j]:
                new_pop.append(population[j])
                break
    return new_pop


# define the crossover function
def crossover(parent1, parent2):
    # select a random crossover point
    split = random.randint(1, n-1)
    # create two children by swapping substrings of their parents
    child1 = parent1[:split] + parent2[split:]
    child2 = parent2[:split] + parent1[split:]
    return child1, child2

# define the mutation function
def mutation(individual):
    # select a random position to mutate and a random value to place there
    pos = random.randint(0, n-1)
    val = random.randint(0, n-1)
    # replace the old value with the new value
    return individual[:pos] + [val] + individual[pos+1:]

# initialize the population
population = [[random.randint(0, n-1) for _ in range(n)] for _ in range(pop_size)]

# display initial population
print("Initial Population:")
for individual in population:
    print(individual)

# run the genetic algorithm
for generation in range(num_generations):
    # selection
    population = selection(population)

    # crossover
    new_population = []
    for i in range(pop_size//2):
        parent1, parent2 = random.sample(population, 2)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(child1)
        new_population.append(child2)

    # mutation
    for i in range(pop_size):
        if random.random() < 0.1:
            new_population[i] = mutation(new_population[i])

    population = new_population

    # display current population
    print("\nGeneration:", generation+1)
    for individual in population:
        print(individual)

    # check for solution
    for individual in population:
        if fitness(individual) == 0:
            print("\nSolution found:", individual)
            break

# display final population
print("\nFinal Population:")
for individual in population:
    print(individual)
