s=0
fil="C:/GitHub/set2/1/input.txt"
f = open(fil,'r')
lines = f.readlines()
lines.append('\n')
l=[]
for line in lines:
    if(line!='\n'):
        s = s + int(line)
    else:
        l.append(s)
        s=0

mx,final_sum=0,0
for i in range(3):
    mx = max(l)
    final_sum += mx
    l.remove(mx)

print('part 2 = ',final_sum)