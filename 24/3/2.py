#simon parker
import re

path = "input.txt"

with open(path, "r") as f:
  lines = [x.strip('\n') for x in f.readlines()] 
  f.close()

pattern = "mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)|do\(\)|don't\(\)"
sum = 0
flag = 1

for data in lines:
  done = False
  while not done:
    command = re.search(pattern, data)
    if command is not None:
      match command.group()[0:3]:
        case "mul":
          operands = [int(x) for x in command.group()[4:-1].split(',')]
          sum += flag * operands[0] * operands[1]
        case "do(":
          flag = 1
        case "don":
          flag = 0
        case _:
          print("fail")
      data = data[command.span()[1]:]
    else:
      done = True
  
print(sum)
