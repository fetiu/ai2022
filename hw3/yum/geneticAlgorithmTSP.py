import random

POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수		

#서울=0, 인천=1, 대전=2, 춘천=3, 강릉=4, 대구=5, 울산=6, 부산=7, 광주=8
distance = [
    [0, 30, 140, 75, 168, 237, 303, 325, 268],
    [30, 0, 140, 105, 198, 247, 315, 334, 257],
    [140, 140, 0, 173, 205, 119, 190, 200, 141],
    [75, 105, 173, 0, 205, 119, 190, 200, 141],
    [168, 198, 205, 102, 0, 213, 247, 287, 340],
    [237, 247, 119, 238, 213, 0, 71, 88, 173],
    [303, 315, 190, 293, 247, 71, 0, 44, 222],
    [325, 334, 200, 323, 287, 88, 44, 0, 202],
    [268, 257, 141, 313, 340, 173, 222, 202, 0]]

# 염색체를 클래스로 정의한다. 
class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		# 유전자는 리스트로 구현된다. 
        self.fitness = 0		# 적합도
        if len(self.genes)==0:	# 염색체가 초기 상태이면 초기화한다. 
            self.genes = random.sample(range(1,9), 8)
    def cal_fitness(self):		# 적합도를 계산한다. 
        self.fitness = 0
        value = 0
        value += distance[0][self.genes[0]]
        for i in range(SIZE-1):
            value += distance[self.genes[i]][self.genes[i+1]]
        value += distance[self.genes[7]][0]
        self.fitness = value
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

# 염색체와 적합도를 출력한다. 
def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i += 1
    print("")

# 선택 연산
def select(pop):
    max_value  = sum([c.cal_fitness() for c in population])
    pick    = random.uniform(0, max_value)
    current = 0
    
    # 룰렛휠에서 어떤 조각에 속하는지를 알아내는 루프
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c

# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)
    two = random.sample(range(SIZE), 2)
    index1 = min(two)
    index2 = max(two)
#    print(index1, index2)
    child1 = [0]*8
    child2 = [0]*8
    child1[index1:index2] = father.genes[index1:index2]
    i = 0
    for j in range(8):
        if mother.genes[j] not in child1:
            child1[i] = mother.genes[j]
        i+=1
        
    child2[index1:index2] = mother.genes[index1:index2]
    i = 0
    for j in range(8):
        if father.genes[j] not in child2:
            child2[i] = father.genes[j]
        i+=1

#    print(father.genes, mother.genes)
#    print(child1, child2)
    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            #c.genes[i] = random.randrange(8)
            index1, index2 = random.sample(range(SIZE), 2)
            c.genes[index1], c.genes[index2] = c.genes[index2], c.genes[index1]

# 메인 프로그램
population = []
i=0

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness())
print("세대 번호=", count)
print_p(population)
count=1

while population[0].cal_fitness() > 1020:
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식 세대가 부모 세대를 대체한다. 
    # 깊은 복사를 수행한다. 
    population = new_pop.copy();    
    
    # 돌연변이 연산
    for c in population: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness())
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 100 : break