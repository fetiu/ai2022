import random

POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수
MIN_DISTANCE = 1018

map = [
        [0, 30, 140, 75, 168, 237, 303, 325, 268],
        [30, 0, 140, 105, 198, 247, 315, 334, 257],
        [140, 140, 0, 173, 205, 119, 190, 200, 141],
        [75, 105, 173, 0, 102, 238, 293, 323, 313],
        [168, 198, 205, 102, 0, 213, 247, 287, 340],
        [237, 247, 119, 238, 213, 0, 71, 88, 173],
        [303, 315, 190, 293, 247, 71, 0, 44, 222],
        [325, 334, 200, 323, 287, 88, 44, 0, 202],
        [268, 257, 141, 313, 340, 173, 222, 202, 0]
    ]


# 염색체를 클래스로 정의한다.
class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		# 유전자는 리스트로 구현된다.
        self.fitness = 0		# 적합도
        if len(self.genes)==0:	# 염색체가 초기 상태이면 초기화한다.
            self.genes = [0,1,2,3,4,5,6,7,8]
            random.shuffle(self.genes)

    def cal_fitness(self):		# 적합도를 계산한다.
        self.fitness = 0;
        distance = 0;
        current_city  = 0
        for next_city in self.genes:
            distance += map[current_city][next_city]
            current_city = next_city
        distance += map[current_city][0]
        self.fitness = (MIN_DISTANCE/distance)*100
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
    # 중복없이 두개 선택
    return random.sample(pop, 2);

def splice(slice, origin):
    diff = [x for x in origin if x not in slice]
    return diff + slice

# 교차 연산
def crossover(pop):
    mother, father = select(pop)
    i = random.randint(1, SIZE-4)
    child1 = splice(father.genes[i:i+4], mother.genes)
    child2 = splice(mother.genes[i:i+4], father.genes)
    return (child1, child2)

# 돌연변이 연산
def mutate(c):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(SIZE), 2)
        c.genes[i], c.genes[j]  = c.genes[j], c.genes[i]

# 메인 프로그램
population = []
i=0

# 초기 염색체를 생성하여 객체 집단에 추가한다.
while i<POPULATION_SIZE:
    population.append(Chromosome())
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

while population[0].cal_fitness() < 100:
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population);
        new_pop.append(Chromosome(c1));
        new_pop.append(Chromosome(c2));

    for c in new_pop: mutate(c)

    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    new_pop.append(population[0])

    # 자식 세대가 부모 세대를 대체한다.
    # 깊은 복사를 수행한다.
    population = new_pop.copy();

    # 돌연변이 연산

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 5000 : break;
print('shortest path:', population[0], '=', (population[0].cal_fitness()/100)*MIN_DISTANCE)