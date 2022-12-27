pointsA = 0
pointsB = 0
point_value = {}

# Using readlines
input_file = open('C:/GitHub/set2/2/input.txt', 'r')
lines = input_file.readlines()

# a = Rock / Paper / Scissor
# b = Rock / Paper / Scissor
def RockPaperScissorsA(a, b):
  global pointsA
  point_value["X"] = 1 # Rock
  point_value["Y"] = 2 # Paper
  point_value["Z"] = 3 # Scissor
  
  pointsA += point_value[b]

  # Dirty check
  if  ( (a == "A" and b == "X") 
     or (a == "B" and b == "Y") 
     or (a == "C" and b == "Z")):
    pointsA += 3 # Draw

  elif( (a == "A" and b == "Y") 
     or (a == "B" and b == "Z") 
     or (a == "C" and b == "X")):
    pointsA += 6 # Win

  else:
    pointsA += 0 # Lose

# a = Rock / Paper / Scissor
# b = Lose / Draw / Win
def RockPaperScissorsB(a, b):
  global pointsB
  point_value["X"] = 0 # Lose
  point_value["Y"] = 3 # Draw
  point_value["Z"] = 6 # Win
  
  pointsB += point_value[b]

  # Dirty check
  if  ( (a == "A" and b == "Z") 
     or (a == "B" and b == "Y") 
     or (a == "C" and b == "X")):
    pointsB += 2 # Paper

  elif( (a == "A" and b == "X") 
     or (a == "B" and b == "Z") 
     or (a == "C" and b == "Y")):
    pointsB += 3 # Scissor

  else:
    pointsB += 1 # Rock

# Read line for line
for line in lines:
  x = line.split()
  RockPaperScissorsA(x[0], x[1])
  RockPaperScissorsB(x[0], x[1])

print("part 1 = " + str(pointsA))
print("part 2 = " + str(pointsB))