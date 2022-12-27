import re

g = open('input.txt').readlines()
for i in range(len(g)): g[i] = g[i].strip()

sum = 0
con = {'0' : 0, '2' : 2, '1' : 1, '-' : -1, '=' : -2}
for n in g:
	cur = 0
	for i in range(len(n) - 1,  - 1, -1):
		cur += pow(5, len(n) - i - 1) * con[n[i]]
	sum += cur
f = 1
while pow(5, f + 1) <= sum: f += 1
def look(n, pla, sum, dig):
	for i in con:
		down = n + pow(5, pla - 1) * con[i]
		if down == sum:
			print(dig + i + ((pla - 1) * '0'))
		else:
			rest = down
			if down > sum:
				for j in range(pla + 1):
					rest -= 2 * pow(5, j)
				if rest < sum: look(down, pla - 1, sum, dig + i)
			elif down < sum:
				for j in range(pla + 1):
					rest += 2 * pow(5, j)
				if rest > sum: look(down, pla - 1, sum, dig + i)

look(0, f + 1, sum, "")