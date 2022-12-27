import functools

with open("C:/GitHub/set2a/13/input.txt") as file:
    data = file.read().split("\n")

pairs = [[]]

i = 0
for line in data:
    if not line: continue

    l = eval(line)
    pairs[-1].append(l)

    if i == 1:
        pairs.append([])
    i = (i + 1)%2

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l == r:
            return None
        else:
            return False
    elif isinstance(l, list) and isinstance(r, list):
        for ll, rr in zip(l, r):
            res = compare(ll, rr)

            if res == False or res == True:
                return res
        if len(l) < len(r):
            return True
        elif len(r) < len(l):
            return False
        else:
            return None
    elif isinstance(l, list):
        return compare(l, [r])
    elif isinstance(r, list):
        return compare([l], r)

def compare_key(l, r):
    res = compare(l, r)

    if res == True:
        return -1
    elif res == False:
        return 1
    else:
        return 0
key = functools.cmp_to_key(compare_key)

final = 0
for i,pair in enumerate(pairs[:-1]):
    res=compare(pair[0], pair[1])
    if res:
        final += i+1

print("part 1 = ", final)

pairs.append([[[2]], [[6]]])
sorted_pairs = list(sorted([a for b in pairs for a in b], key=key))

print("part 2 = ", (sorted_pairs.index([[2]])+1) * (sorted_pairs.index([[6]])+1))