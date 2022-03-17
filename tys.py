import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input("Enter number:"))
besttemp = 40

for i in input("Enter number).split():
    t = int(i)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(t, file=sys.stderr, flush=True)

    if abs(t) < abs(besttemp):
        besttemp = t
    if abs(t) == abs(besttemp) and t > 0:
        besttemp = t

if besttemp == 40:
    c = besttemp - besttemp
    print(c)
else:
    print("try later")
print(c)
