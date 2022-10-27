import random

POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수

def gen_queen():
    return random.randrange(8)

# 염색체를 클래스로 정의한다.
class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		# 유전자는 리스트로 구현된다.
        self.fitness = 0		# 적합도
        if len(self.genes)==0:	# 염색체가 초기 상태이면 초기화한다.
            i = 0
            while i<SIZE:
                self.genes.append(gen_queen())
                i += 1

    def cal_fitness(self):		# 적합도를 계산한다.
        self.fitness = 0;
        value = 28
        for i in range(SIZE):
            for j in range (i+1, SIZE):
                if (self.genes[i] == self.genes[j] or
                    abs(self.genes[i] - self.genes[j]) == abs(i - j)):
                    value -= 1
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
    # 오름차순 정렬로 좋은 유전자가 큰 인덱스 값을 갖게 한 뒤, 그 값에 비례하여 룰렛에 더 많이 삽입
    pop.sort(key=lambda x: x.cal_fitness())
    roulette = [c for i, c in enumerate(pop) for _ in range((i+1)**i)] # NOTE: (0+1)^0 = 1

    # 중복없이 두개 선택
    return random.sample(roulette, 2);

# 교차 연산
def crossover(pop):
    mother, father = select(pop)
    index = random.randint(1, SIZE-2)
    child1 = father.genes[:index] + mother.genes[index:]
    child2 = mother.genes[:index] + father.genes[index:]
    return (child1, child2)

# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes[i] = gen_queen()

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

while population[0].cal_fitness() < 28:
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population);
        new_pop.append(Chromosome(c1));
        new_pop.append(Chromosome(c2));

    # 자식 세대가 부모 세대를 대체한다.
    # 깊은 복사를 수행한다.
    population = new_pop.copy();

    # 돌연변이 연산
    for c in population: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1
    if count > 2000 : break;