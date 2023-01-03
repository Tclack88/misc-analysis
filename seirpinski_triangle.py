# I saw a social media post that drawing a midpoint point between two vertices
# of a triangle and then continuing to find the midpoing between that last 
# point and a random vertex will result in a seripinski triangle
# This was just a check that it results in the pattern (it does indeed)
from random import choice
import matplotlib.pyplot as plt

starters = [(0,0),(1,0),(.5,.866)]

def midpoint(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return (x1 + x2)/2, (y1 + y2)/2

coords = [midpoint(starters[0],starters[1])]

for _ in range(10000):
    coords.append(midpoint(choice(starters),coords[-1]))

xs = [x for x,y in coords]
ys = [y for x,y in coords]

plt.scatter(xs,ys, s=1)
plt.show()
