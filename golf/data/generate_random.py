import random
import sys

random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument

n = random.randint(2, 100)
m = random.randint(1, 500)


print(n,m)

for i in range(n):
    for j in range(m-1):
        s = random.randint(-99,99)
        out = ""
        if s > 0:
          out = "+"
        out += str(s)
        print(out, end=" ")
    s = random.randint(-99,99)
    out = ""
    if s > 0:
      out = "+"
    out += str(s)
    print(out)
