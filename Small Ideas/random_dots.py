import matplotlib.pyplot as plt
import random

x_coords = list(random.randint(1,100))
y_coords = list(random.randint(1,100))

plt.scatter(x_coords, y_coords, c = "red", s = 15)

plt.show()

