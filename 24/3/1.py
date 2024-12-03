#simon parker
import re

path = "input.txt"

with open(path, "r") as f:
  lines = [x.strip('\n') for x in f.readlines()] 
  f.close()

pattern = "mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)"
sum = 0
for data in lines:
  done = False
  while not done:
    match = re.search(pattern, data)
    if match is not None:
      operands = [int(x) for x in match.group()[4:-1].split(',')]
      sum += operands[0] * operands[1]
      #data = data[0:match.span()[0]] + data[match.span()[1]:]
      data = data[match.span()[1]:]
    else:
      done = True
  
print(sum)

