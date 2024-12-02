#simon parker

path = "input.txt"

with open(path, "r") as f:
  lines = [x.strip().split() for x in f.readlines()] 
  f.close()

#these 2 functions return True if they are safe or False if not
def inc_safely(l, damped):
  for i in range(len(l) - 1):
    if l[i] >= l[i + 1]:
      if not damped:
        return False
      else:
        t1 = l.copy()
        t2 = t1.copy()
        t1.pop(i) #sometimes you are the problem
        t2.pop(i + 1) #sometimes it's your neighbor
        return inc_safely(t1, False) or inc_safely(t2, False)
    elif l[i + 1] - l[i] > 3:
      if not damped:
        return False
      else:
        t1 = l.copy()
        t2 = t1.copy()
        t1.pop(i)
        t2.pop(i + 1)
        return inc_safely(t1, False) or inc_safely(t2, False)
  return True


def dec_safely(l, damped):
  for i in range(len(l) - 1):
    if l[i] <= l[i + 1]:
      if not damped:
        return False
      else:
        t1 = l.copy()
        t2 = t1.copy()
        t1.pop(i)
        t2.pop(i + 1)
        return dec_safely(t1, False) or dec_safely(t2, False)
    elif l[i] - l[i + 1] > 3:
      if not damped:
        return False
      else:
        t1 = l.copy()
        t2 = t1.copy()
        t1.pop(i)
        t2.pop(i + 1)
        return dec_safely(t1, False) or dec_safely(t2, False)
  return True

sum = 0

for line in lines:
  int_line = [int(x) for x in line]
  sum = sum + 1 if inc_safely(int_line, True) or dec_safely(int_line, True) else sum

print(sum)
