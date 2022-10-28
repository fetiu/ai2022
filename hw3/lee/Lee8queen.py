import random
import time

POPULATION_SIZE = 6
MUTATION_RATE = 0.1		
SIZE = 8				

def queens_gen():
    return random.randrange(8)


class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		
        self.fitness = 0		
        if len(self.genes)==0:	
            i = 0
            while i<SIZE:
                self.genes.append(queens_gen())
                i += 1

    def cal_fitness(self):		
        self.fitness = 0;
        gen_list = list(map(int, self.genes)) 
        value = 0
        for i in range(SIZE):  
            col = gen_list[i]
            for j in range(SIZE):
                if j == i:
                    continue
                if gen_list[j] == col:
                    continue
                if j + gen_list[j] == i + col:
                    continue
                if j - gen_list[j] == i - col:
                    continue
              
                value += 1
        self.fitness = value/2
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i += 1
    print("")

def select(pop):
    # Chromosome을 키 삼아 조회하는 룰렛 딕셔너리를 생성
    # 선택 확률을 최대화 하기 위해 적합도에 100 제곱을 취함
    roulette = {c:c.cal_fitness()**100 for c in pop}
    max_value  = sum(roulette.values())
    pick    = random.uniform(0, max_value)
    current = 0

    # 룰렛휠에서 어떤 조각에 속하는지를 알아내는 루프
    for c in pop:
        current += roulette[c]
        if current > pick:
            return c


def crossover(pop):
    father = select(pop)
    mother = select(pop)
    index = random.randint(1, SIZE-2)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (child1, child2)


def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes[i] = queens_gen()


population = []
i=0


while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

while population[0].cal_fitness() < 28:
    new_pop = []


    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population);
        new_pop.append(Chromosome(c1));
        new_pop.append(Chromosome(c2));


    population = new_pop.copy();

    for c in population: mutate(c)

    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 2000 : break;