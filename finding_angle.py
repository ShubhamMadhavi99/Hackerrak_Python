import math
from math import acos, degrees

A = int(input())
B = int(input())
C = math.sqrt(A*A + B*B)
print(C)

ABC = degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
print(ABC)