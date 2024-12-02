#simon parker

path = "input.txt"

with open(path, "r") as f:
  lines = [x.strip().split() for x in f.readlines()] 
  f.close()

#these 2 functions return True if they are safe or False if not
def inc_safely(l):
  for i in range(len(l) - 1):
    if l[i] >= l[i + 1]:
      return False
    elif l[i + 1] - l[i] > 3:
      return False
  return True

def dec_safely(l):
  for i in range(len(l) - 1):
    if l[i] <= l[i + 1]:
      return False
    elif l[i] - l[i + 1] > 3:
      return False
  return True

sum = 0

for line in lines:
  line = [int(x) for x in line]
  sum = sum + 1 if inc_safely(line) or dec_safely(line) else sum

print(sum)
