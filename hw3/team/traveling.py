import random
import matplotlib.pyplot as plt

MIN_DISTANCE = 1018
POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수

cities = {
    'su': {'ic': 30, 'dj': 140, 'cc': 75, 'gr': 168,
           'dg': 237, 'us': 303, 'ps': 325, 'gj': 268},
    'ic': {'su': 30, 'dj': 140, 'cc': 105, 'gr': 198,
           'dg': 247, 'us': 315, 'ps': 334, 'gj': 257},
    'dj': {'su': 140, 'ic': 140, 'cc': 173, 'gr': 205,
           'dg': 119, 'us': 190, 'ps': 200, 'gj': 141},
    'cc': {'su': 75, 'ic': 105, 'dj': 173, 'gr': 102,
           'dg': 238, 'us': 293, 'ps': 323, 'gj': 313},
    'gr': {'su': 168, 'ic': 198, 'dj': 205, 'cc': 102,
           'dg': 213, 'us': 247, 'ps': 287, 'gj': 340},
    'dg': {'su': 237, 'ic': 247, 'dj': 119, 'cc': 238,
           'gr': 213, 'us': 71, 'ps': 88, 'gj': 173},
    'us': {'su': 303, 'ic': 315, 'dj': 190, 'cc': 293,
           'gr': 247, 'dg': 71, 'ps': 44, 'gj': 222},
    'ps': {'su': 325, 'ic': 334, 'dj': 200, 'cc': 323,
           'gr': 287, 'dg': 88, 'us': 44, 'gj': 202},
    'gj': {'su': 268, 'ic': 257, 'dj': 141, 'cc': 313,
           'gr': 340, 'dg': 173, 'us': 222, 'ps': 202},
}

# 염색체를 클래스로 정의한다.
class Chromosome:
    def __init__(self, g=[]):
        self.genes = g.copy()		# 유전자는 리스트로 구현된다.
        self.fitness = 0		# 적합도
        if len(self.genes)==0:	# 염색체가 초기 상태이면 초기화한다.
            self.genes = ['ic', 'dj', 'cc', 'gr', 'dg', 'us', 'ps', 'gj']
            random.shuffle(self.genes)

    def cal_fitness(self):		# 적합도를 계산한다.
        self.fitness = 0;
        distance = 0;
        now  = 'su'
        for next in self.genes:
            distance += cities[now][next]
            now = next
        distance += cities[now]['su']
        self.fitness = MIN_DISTANCE/distance*100
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
data = []

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
    data.append(population[0].cal_fitness())
    if count > 1000 : break;

print(f'shortest path: sum({population[0]}) = {int(MIN_DISTANCE/population[0].cal_fitness()*100)}')
plt.plot(data)
plt.show()
