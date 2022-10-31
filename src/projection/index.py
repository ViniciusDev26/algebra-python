import matplotlib.pyplot as plt

from projection2d import projection2DX
from projection2d import projection2DY

fig, ax = plt.subplots()

# original 2d point
originPoint = [0, 0]
vector = [4, 2]
ax.plot([originPoint[0], vector[0]], [originPoint[1], vector[1]], 'b')

# projection 2dX
resultX = projection2DX(vector)
ax.plot([originPoint[0], resultX[0]], [originPoint[1], resultX[1]], 'r')
ax.axis([0, 10, -2, 10])

# projection 2dX
resultY = projection2DY(vector)
ax.plot([originPoint[0], resultY[0]], [originPoint[1], resultY[1]], 'black')
ax.axis([-2, 10, -2, 10])

plt.show()