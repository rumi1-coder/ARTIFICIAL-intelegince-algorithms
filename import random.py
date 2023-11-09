import random
n=int(input('enter a number'))
population_size=10
number_generations=100
population=[[random.randint(0,n-1) for _ in range(n)] for _ in range(10)]

for individual in population:
    print(individual)

def fitness(p):
    clashes=0
    for i in range(10):
        for j in range(n-1):
            if p[i]==p[j]:
                clashes+=1
    return clashes
def crossover(p1,p2):
    split=random.randint(1,n-1)
    c1=p1[:split]+p2[split:]
    return c1,c2
def mutation(p):
    val=random.randint(1,n-1)
    return i[:pos]+[val]+[pos+1:]
def selection(population):
   fits=[fitness(p) for p in po]
   fitssum=sum(fits)
   probs=[f/fin for f in fits]
   cum=[sum(bro[:i+1]) for iin range(len(probs))]
   new =[]
   for i in range(popsize):
       for j in range()
       if r<sum[]
       
for genera in range(nyumm):
    population=selection(polulation)
    for i in range(population_size/2):
        p1,p2=random.sample(polulatio,2)
        
        