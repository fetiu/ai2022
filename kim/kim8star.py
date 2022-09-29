from copy import deepcopy
import time

def tile(num):
    return [' ','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣'][num]

def inside(pos):
    x, y = pos
    return not (x < 0 or x > 2 or y < 0 or y > 2)

class EightPuzzle:
    class State:
        def __init__(self, tiles, moves):
            self.tiles = tiles
            self.moves = moves
            self.cost = 0

        def locate(self, tile):
            for y, row in enumerate(self.tiles):
                if tile in row:
                    return (row.index(tile), y)

        def count_diff(self, tiles):
            cnt = 0
            for y in range(3):
                for x in range(3):
                    if tiles[y][x] == tile(0):
                        continue
                    if tiles[y][x] != self.tiles[y][x]:
                        cnt += 1
            return cnt

    def __init__(self, str_nine_nums):
        nine_nums = map(int, str_nine_nums.strip())
        tile_list = list(map(tile, nine_nums))
        tiles = [tile_list[0:3], tile_list[3:6], tile_list[6:9]]
        self.state = EightPuzzle.State(tiles, 0)

    def draw(self):
        print('- step', self.state.moves, '-')
        for row in self.state.tiles:
            print(f'{row[0]} {row[1]} {row[2]}')
        print()

    def get_next_states(self):
        next_states = []
        x,y = self.state.locate(tile(0))
        adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        next_pos = [(x+dx, y+dy) for dx,dy in adjacent]
        valid_pos = list(filter(inside, next_pos))
        for nx, ny in valid_pos:
            tiles = deepcopy(self.state.tiles)
            tiles[y][x], tiles[ny][nx] = tiles[ny][nx], tiles[y][x]
            state = EightPuzzle.State(tiles, self.state.moves + 1)
            next_states.append(state)
        return next_states

class AStarSolver:
    def __init__(self, target):
        self.target = target
        return

    def h(self, state):
        return self.target.state.count_diff(state.tiles)
        # displacment = 0
        # for num in range(1, 9):
        #     i, j = self.target.state.locate(tile(num))
        #     x, y = state.locate(tile(num))
        #     displacment += abs(i-x) + abs(j-y)
        # return displacment

    def g(self, state):
        return state.moves

    def f(self, state):
        return self.g(state) + self.h(state)

    def solve(self, puzzle):
        queue = [puzzle.state]
        visit = []
        while len(queue) > 0:
            puzzle.state = queue.pop(0)
            puzzle.draw()
            if puzzle.state.tiles == self.target.state.tiles:
                print("success")
                break

            for state in puzzle.get_next_states():
                if state not in visit and state not in queue:
                    state.cost = self.f(state)
                    # print(state.tiles, state.cost, state.moves)
                    # time.sleep(0.5)
                    queue.append(state)
            visit.append(puzzle.state)
            queue.sort(key=lambda x: x.cost)
            # print([state.tiles for state in queue])

target = EightPuzzle("123456780")
solver = AStarSolver(target)

# puzzle = EightPuzzle(input("type 9 numbers (0-8): "))
puzzle = EightPuzzle("152703468")
# puzzle = EightPuzzle("123046758")
solver.solve(puzzle)

