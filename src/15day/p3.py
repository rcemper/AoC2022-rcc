from collections import defaultdict
import re
lines = open('input.txt').readlines()
lines = [line.strip() for line in lines]

goal_line = 2000000
search_min_x, search_max_x = 0, 4000000
search_min_y, search_max_y = 0, 4000000
# goal_line = 10
# search_min_x, search_max_x = 0, 20
# search_min_y, search_max_y = 0, 20


def x_just_out_of_range(sensor_pos, sensor_range, y):
    sx, sy = sensor_pos
    delta_y = abs(y - sy)
    delta_x = sensor_range - delta_y
    return sx - delta_x-1, sx + delta_x +1

def just_out_of_range(sensor_pos, sensor_range):
    sy, sx = sensor_pos
    search_y_min = max(search_min_y, sy - sensor_range-1)
    search_y_max = min(search_max_y, sy + sensor_range+2)
    border = set()
    for y in range(search_y_min, search_y_max):
        for x in x_just_out_of_range((sx, sy), manhattan, y):
            if x < search_min_x or x >= search_max_x:
                continue
            border.add((x, y))
    return border

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

non_beacon_tiles = set()
just_out_of_range_sensor = defaultdict(set)
sensor_ranges = dict()

for i, line in enumerate(lines):
    print(i) 
    # Get all numbers including negative ones
    sx, sy, bx, by = [int(x) for x in re.findall(r'-?\d+', line)]
    manhattan = manhattan_distance(sx, sy, bx, by)
    sensor_ranges[(sx, sy)] = manhattan

    # Find all positions where no beacon can be placed for part 1
    for y in range(sy - manhattan, sy + manhattan + 1):
        if y == goal_line: # Only look at the goal line
            for x in range(sx - manhattan, sx + manhattan + 1): # Very ugly but works
                # Skip the beacon
                if x == bx and y == by:
                    continue

                if manhattan_distance(sx, sy, x, y) <= manhattan:
                    if y == goal_line: 
                        non_beacon_tiles.add((x, y))

    # Find all positions just out of reach of this sensor for part 2
    just_out_of_range_sensor[(sx, sy)] = just_out_of_range((sx, sy), manhattan)


count_line = 0
for x, y in non_beacon_tiles: 
    if y == goal_line: 
        count_line += 1
print('part 1', count_line)


# Determine which tiles are in the overlap of two sensors as our point must be on the border of at least two sensors
all_overlaps = set()
for i, key1 in enumerate(just_out_of_range_sensor.keys()): 
    print(i)
    with_overlap = set()
    for j, key2 in enumerate(just_out_of_range_sensor.keys()): 
        if i != j: 
            # Find the overlap between sets and add it to to_remove
            with_overlap |= just_out_of_range_sensor[key1] & just_out_of_range_sensor[key2]
    
    all_overlaps |= with_overlap

# Determine which of the overlapping tiles are actually in range of another sensor and remove them    
to_remove = set()
for j, tile in enumerate(all_overlaps):
    for i, sensor in enumerate(sensor_ranges.keys()):
        if manhattan_distance(sensor[0], sensor[1], tile[0], tile[1]) <= sensor_ranges[sensor]:
            to_remove.add(tile)
all_overlaps -= to_remove      

x, y = all_overlaps.pop() # Assume there is only one
print("Part 2", x, y, x*4000000+y)
