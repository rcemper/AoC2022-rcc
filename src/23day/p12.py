import re
import functools
import itertools
import collections
from collections import defaultdict
from collections import Counter
import sys
inf = 'C:/GitHub/set2/23/input.txt'

ll = [x for x in open(inf).read().strip().split('\n')]

# part 2 will probably make the board really big so i'll use a set of coords instead of a 2d map

elves = list()
for i in range(len(ll)):
	for j in range(len(ll[0])):
		#print(i,j,ll[i][j])
		if ll[i][j] == "#":
			elves.append((i,j))

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
TEST = [(0, 1), (0, 1), (1, 0), (1, 0)]
def addt(x, y):
	if len(x) == 2:
		return (x[0] + y[0], x[1] + y[1])
	return tuple(map(sum, zip(x, y)))

def round(elves, round_idx):
	elves = list(tuple(elves)) # copy
	testset = set(elves) # lookups
	proposed = []
	for i in range(len(elves)):
		elf = elves[i]
		any_adj = False
		for dx in range(-1, 2):
			for dy in range(-1, 2):
				if (dx != 0 or dy != 0) and (elf[0]+dx, elf[1]+dy) in testset:
					any_adj = True
					break
		if not any_adj:
			proposed.append(elf)
			continue
		for pdir in range(4):
			pdir = (pdir + round_idx) % 4
			dr = DIRS[pdir]
			adj = addt(dr, elf)
			works = True
			for test in range(-1, 2):
				testloc = (TEST[pdir][0] * test, TEST[pdir][1] * test)
				if addt(testloc, adj) in testset:
					works = False
					break
			if works:
				proposed.append(adj)
				break
		if not works: # all of them were works=False
			proposed.append(elf)
	new_pos = []
	for i in range(len(elves)):
		if proposed.count(proposed[i]) > 1:
			new_pos.append(elves[i])
		else:
			new_pos.append(proposed[i])
	if len(proposed) != len(elves) or len(new_pos) != len(elves):
		raise Exception("fuck")
	#printpts(new_pos)
	return new_pos

def printpts(dots):
	ys = [pos[0] for pos in dots]
	xs = [pos[1] for pos in dots]
	for y in range(min(ys), max(ys)+1):
		s = ""
		for x in range(min(xs), max(xs)+1):
			if (y,x) in dots:
				s += "X"
			else:
				s += " "
		print('??? ',s)
	print()

for i in range(1000000):
	new_elves = round(elves, i)
	if i == 10:
		ys = [pos[0] for pos in elves]
		xs = [pos[1] for pos in elves]
		print('part 1 = ',(max(ys)-min(ys)+1) * (max(xs)-min(xs)+1) - len(elves))
	if tuple(new_elves) == tuple(elves):
		print('part 2 = ',i+1)
		break
	elves = new_elves
