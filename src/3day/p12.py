import string
atoz = string.ascii_lowercase + string.ascii_uppercase

with open("C:/GitHub/set2/3/input.txt") as f:
    inputs = f.read().splitlines()

total1 = sum(
    atoz.index("".join(set(pack[: len(pack) // 2]) & set(pack[len(pack) // 2 :]))) + 1
    for pack in inputs
)

total2 = sum(
    atoz.index("".join(set.intersection(*map(set, group)))) + 1
    for group in (inputs[i : i + 3] for i in range(0, len(inputs), 3))
)

print('part 1 = '+ str(total1))
print('part 2 = '+ str(total2))