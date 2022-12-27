s,max=0,0
fil="C:/GitHub/set2/1/input.txt"
f = open(fil,'r')
lines = f.readlines()
lines.append('\n')

for line in lines:
    if(line!='\n'):
        s = s + int(line)
    else:
        if(max<s):
            max=s
        s=0
            
print('part 1 =',max)