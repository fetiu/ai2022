import copy

def find_index(puzzle, num):
    index = puzzle.find(num)
    i = index//3
    j = index - i*3
    return i, j

def get_adjacent(puzzle):
    i, j = find_index(puzzle, "0")

    map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []

    for k in map:
        if not ((i+k[0] < 0) or (i+k[0] > 2) or (j + k[1] < 0) or (j+k[1] > 2)):
            result.append(k)
    return result

def next_states(puzzle, adjacent):
    i, j = find_index(puzzle, "0")

    move_to = []
    for adj in adjacent:
        move_to.append((i+adj[0], j+adj[1]))

    result = []
    for p in move_to:
        puzzle_list = []
        for a in puzzle:
            puzzle_list.append(a)
        blank_indx = i*3 + j
        dest_indx = p[0]*3 + p[1]
        puzzle_list[blank_indx], puzzle_list[dest_indx] = puzzle_list[dest_indx], puzzle_list[blank_indx]

        result.append("".join(puzzle_list))

    return result


def print_steps(routes):

    for route in routes:
        puzzle = route[0]
        i = routes.index(route)
        g = i
        h = route[1]
        f = g+h
        print(f"step {i}: g={g}, h={h}, f={f}")

        for k in range(0, 9, 3):
            print(puzzle[k:k+3])
        print()


def h_score(puzzle, goal):
    h_point = 0

    for num in range(len(puzzle)):
        i, j = find_index(puzzle, str(num))
        x, y = find_index(goal, str(num))

        # 총 숫자의 차이를 구함
        h = abs(i-x) + abs(j-y)
        h_point += h
    return h_point

def solve(puzzle, goal):
    path = []
    check = {puzzle: 1}

    path.append([[puzzle, h_score(puzzle, goal)]])
    while path:
        curr_route = path.pop(0)
        curr_state = curr_route[-1][0]

        if curr_state == goal:
            route = curr_route
            return route
        g = len(curr_route)

        if check[curr_state] != g:
            continue

        for state in next_states(curr_state, get_adjacent(curr_state)):
            state_g = g + 1
            if state in check:
                if state_g < check[state]:
                    check[state] = state_g
                    to_add_state = copy.deepcopy(curr_route)
                    to_add_state.append([state, h_score(state, goal)])
                    path.append(to_add_state)

            else:
                check[state] = state_g
                to_add_state = copy.deepcopy(curr_route)
                to_add_state.append([state, h_score(state, goal)])
                path.append(to_add_state)

        path = sorted(path, key=lambda x: x[-1])


pass


puzz1 = "123405678"
puzz2 = "152703468"


result = solve(puzz1, "123456780")
print_steps(result)
