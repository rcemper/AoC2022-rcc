#!/usr/bin/python
f = open("C:/GitHub/set2/4/input.txt", "r")
overlapping = 0

for line in f:
    a = line.split(",")
    prvi, drugi = a[0].split("-"), a[1].split("-")

    if (int(prvi[0]) >= int(drugi[0]) and int(prvi[1]) <= int(drugi[1])) or (int(prvi[0]) <= int(drugi[0]) and int(prvi[1]) >= int(drugi[1])):
        overlapping += 1

print('part 1 = ',overlapping)

f = open("C:/GitHub/set2/4/input.txt", "r")
overlaping = 0
len = 0

for line in f:
    a = line.split(",")
    len += 1
    prvi, drugi = a[0].split("-"), a[1].split("-")

    if int(prvi[1]) < int(drugi[0]) or int(drugi[1]) < int(prvi[0]):
        overlaping += 1

print('part 2 = ',len - overlaping)