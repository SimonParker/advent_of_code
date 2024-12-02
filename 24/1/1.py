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

l1.sort()
l2.sort()

print(sum([abs(x - y) for x, y in zip(l1, l2)]))

