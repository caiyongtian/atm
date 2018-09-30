import time
import sys

a = time.asctime().split()
print(a)

a[-1] = int(a[-1]) + 2

print(a)

for i in a:
    b = sys.stdin(print(i,end=' '))
    print(b)


