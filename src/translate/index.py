import matplotlib.pyplot as plt
from translate2d import translate2d
from translate3d import translate3d

fig, ax = plt.subplots()
bx = plt.figure().add_subplot(projection='3d')

# original 2d point
vector = [4, 2]
ax.plot(vector[0], vector[1], 'bo')

# translated 2d point
result = translate2d(vector, 2, 3)
ax.plot(result[0], result[1], 'ro')
ax.axis([0, 10, 0, 10])


# original 3d point
vector = [4, 2, 2]
bx.plot(vector[0], vector[1], vector[2], 'bo')

# translated 3d point
result = translate3d(vector, 2, 4, 4)
bx.plot(result[0], result[1], result[2], 'ro')
bx.axis([0, 10, 0, 10])

plt.show()