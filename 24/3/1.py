#simon parker
import re

path = "test.txt"

with open(path, "r") as f:
  lines = [x.strip('\n') for x in f.readlines()] 
  f.close()

pattern = "mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)"
sum = 0
for data in lines:
  done = False
  while not done:
    command = re.search(pattern, data)
    if command is not None:
      operands = [int(x) for x in command.group()[4:-1].split(',')]
      sum += operands[0] * operands[1]
      data = data[command.span()[1]:]
    else:
      done = True
  
print(sum)

