#!/usr/bin/python
f = open("C:/GitHub/set2/5/input.txt", "r")
stack1 = []
for i in range(10):
    stack1.append([])

for line in f:
    # Moving crates
    if line[0] == "m":
        a = line.split(" ")
        temp1 = []
        for r in range(0, int(a[1])):
            element = stack1[int(a[3])].pop()
            temp1.insert(0, element)
        stack1[int(a[5])] = stack1[int(a[5])] + temp1

    else:
        # Putting crates onto the stack
        parts = [line[i : i + 4] for i in range(0, len(line), 4)]
        st = 0

        if line.find("[") == -1:
            continue

        for part in parts:
            crka = part[1:2]
            st += 1
            if crka == " ":
                continue
            stack1[st].insert(0, crka)

# Reading top elements
print('part 2 = ', end="")
for h in range(0, 10):
    if len(stack1[h]):
        print(stack1[h].pop(), end="")