#simon parker

path = "input.txt"
l1 = []
l2 = []

with open(path, "r") as f:
  lines = [x.strip().split() for x in f.readlines()]
  f.close()

for line in lines:
  l1.append(int(line[0]))
  l2.append(int(line[1]))

print(sum([x * l2.count(x) for x in l1]))

