from heapq import heapify, heappop, heappush

def find_distances(start, data, interesting, queue, paths):
    heapify(queue)
    seen = set(start)
    while queue:
        steps, valve = heappop(queue)
        steps += 1
        for nxt in data[valve][1]:
            if nxt not in seen:
                seen.add(nxt)
                if nxt in interesting and nxt != start:
                    paths[nxt] = steps
                heappush(queue, [steps, nxt])
    return paths

def path_finder(data, distances, queue, part1=False, end=None):
    best = {}
    heapify(queue)
    while queue:
        time, release, p1, p2, seen = heappop(queue)
        if time == end + 1:
            return -min(best.values())
        (time, valve), (time2, valve2) = (p1, p2) if part1 else sorted([p1, p2])
        for k, v in distances[valve].items():
            if end - (v + 1) <= 0:
                heappush(queue, [end if part1 else min(end, valve2), release, (end, valve), (time2, valve2), seen])
            else:
                if k not in seen:
                    next_time = time + v + (s := k not in seen)
                    next_release = release - (end - next_time) * data[k][0] * s
                    next_seen = sorted(seen + [k])
                    tup_seen = tuple(next_seen)
                    if not tup_seen in best or best[tup_seen] > next_release:
                        best[tup_seen] = next_release
                        heappush(queue, [next_time, next_release, (next_time, k), (time2, valve2), next_seen])

with open("C:/GitHub/set2/16/input.txt", "r") as file:
    data = {(z := x.split(" "))[1] : (int(z[4].strip("rate=").strip(";")), [y.strip(",") for y in z[9:]]) for x in file.read().splitlines()}
    interesting = set([k for k, v in data.items() if v[0] > 0] + ["AA"])
    distances = {x : find_distances(x, data, interesting, [tuple([0, x])], {}) for x in interesting}
    q = [(0, 0, (0, "AA"), (0, "AA"), ["AA"])]
    print("part 1 =", path_finder(data, distances, q[:], part1=True, end=30)) 
    print('part 2 =',path_finder(data, distances, q[:], end=26))