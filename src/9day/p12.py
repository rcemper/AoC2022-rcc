def assertions():
    head = (0, 0)
 
    assert move((0, 0), (1, 1)) == (1, 1)
    assert move((3, 5), (2, 4)) == (5, 9)
 
    # doesn't require movement
    assert (v := get_updated_position((0, 0), head)) == (0, 0), v
    assert (v := get_updated_position((-1, 0), head)) == (-1, 0), v
    assert (v := get_updated_position((0, 1), head)) == (0, 1), v
 
    # requires diagonal movement
    assert (v := get_updated_position((2, 1), head)) == (1, 0), v
    assert (v := get_updated_position((-2, -1), head)) == (-1, 0), v
    assert (v := get_updated_position((-1, -2), head)) == (0, -1), v
 
    # requires horizontal or vertical movement
    assert (v := get_updated_position((2, 0), head)) == (1, 0), v
    assert (v := get_updated_position((-2, 0), head)) == (-1, 0), v
    assert (v := get_updated_position((0, -2), head)) == (0, -1), v
 
    # random testing
    assert (v := get_updated_position((0, 0), (2, 0))) == (1, 0), v
    assert (v := get_updated_position((8, 10), (10, 10))) == (9, 10), v
 
    # tuples = (index of node to be updated, index of target node)
    assert iterate_rope([3, 3, 3, 3]) == ((2, 3), (1, 2), (0, 1))
 
 
def iterate_rope(rope: list) -> tuple:
    return tuple((i - 1, i) for i in range(len(rope) - 1, 0, -1))
 
 
def get_updated_position(updating_node: tuple, target_node: tuple) -> tuple:
    ux, uy = updating_node
    tx, ty = target_node
 
    delta_x = tx - ux
    delta_y = ty - uy
 
    if abs(delta_x) <= 1 and abs(delta_y) <= 1:
        return updating_node
 
    if delta_y == 0:
        return (ux + delta_x // 2, uy)
 
    if delta_x == 0:
        return (ux, uy + delta_y // 2)
 
    return (ux + 1 * delta_x / abs(delta_x), uy + 1 * delta_y / abs(delta_y))
 
 
def get_instructions(path: str) -> list:
    instructions = []
    deltas = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
    }
    for line in open(path, 'r').read().strip().split('\n'):
        direction, quantity = line.split(' ')
 
        instructions.append((deltas[direction], int(quantity)))
 
    return instructions
 
 
def main1(instructions: list, rope_length: int) -> int:
    visited = {(0, 0)}
    rope = [(0, 0)]
 
    for delta, quantity in instructions:
 
        for x in range(quantity):
            rope[-1] = move(rope[-1], delta)
 
            for p1, p2 in iterate_rope(rope):
                rope[p1] = get_updated_position(rope[p1], rope[p2])
 
            if rope[0] != (0, 0) and len(rope) < rope_length:
                rope = [(0, 0)] + rope
 
            visited.add(rope[0])
 
    return len(visited)  # resultado
 
 
def move(vector1: tuple, vector2: tuple) -> tuple:
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])
 
 
if __name__ == '__main__':
    input_data = get_instructions('C:/GitHub/set2/9/input.txt')
    assertions()
 
    print('part 1 = ',main1(input_data, 2))
    print('part 2 = ',main1(input_data, 10))