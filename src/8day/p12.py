#this is more clearly separated between parts 1 and 2

Input = open("C:/GitHub/set2/8/input.txt")
Text  = Input.readlines()
Forest = []
Count = 0
MaxScore = 0

for Line in Text:
    Line = Line.rstrip()
    TreeRow = []
    for i in range(len(Line)):
        TreeRow.append(int(Line[i]))
    Forest.append(TreeRow)

for i in range(len(Forest)):
    Row = Forest[i]
    for j in range(len(Row)):
        Score = [0,0,0,0]
        if (i == 0) or (i == len(Forest)-1) or (j == 0) or (j == len(Row)-1):
            Count += 1
        else:
            Height = int(Row[j])
            #check left trees
            Compare = Row[0:j]
            if Height > max(Compare):
                Count += 1
            else:
                #check right trees
                Compare = Row[j+1: len(Row)]
                if Height > max(Compare):
                    Count += 1
                else:
                    #check trees above
                    Compare = []
                    for k in range(0,i):
                        Compare.append(Forest[k][j])
                    if Height > max(Compare):
                        Count += 1
                    else:
                        Compare = []
                        for l in range(i+1,len(Forest)):
                            Compare.append(Forest[l][j])
                        if Height > max(Compare):
                            Count += 1
            #look left
            for m in range(j-1,-1,-1):
                if Forest[i][m] < Height:
                    Score[0] += 1
                else:
                    Score[0] += 1
                    break
            #look right
            for n in range(j+1,len(Row)):
                if Forest[i][n] < Height:
                    Score[1] += 1
                else:
                    Score[1] += 1
                    break
            #look up
            for o in range(i-1,-1,-1):
                if Forest[o][j] < Height:
                    Score[2] += 1
                else:
                    Score[2] += 1
                    break
            #look down
            for p in range(i+1, len(Forest)):
                if Forest[p][j] < Height:
                    Score[3] += 1
                else:
                    Score[3] += 1
                    break
            # compare score to max known score
            if MaxScore < (Score[0] * Score[1] * Score[2] * Score[3]):
                MaxScore = (Score[0] * Score[1] * Score[2] * Score[3])


print("part 1 = ", Count)
print("part 2 = ", MaxScore)