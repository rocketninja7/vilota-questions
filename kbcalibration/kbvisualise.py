import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Reference: https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid
grid_x, grid_y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))

# Perform transformation here
# Initialise parameters
focal_length = 2
fx = 622
fy = 622
cu = 965
cv = 631
k1 = -0.256
k2 = -0.0015
k3 = 0.0007
k4 = -0.0002

r = lambda t: k1 * t + k2 * t**3 + k3 * t**5 + k4 * t**7

f_theta = np.arctan((grid_x * grid_x + grid_y * grid_y)**0.5 / focal_length)
f_phi = np.arctan2(grid_y, grid_x)

grid_x = r(f_theta) * np.cos(f_phi)
grid_y = r(f_theta) * np.sin(f_phi)

ax = plt.gca()
horizontal_lines = np.stack((grid_x, grid_y), axis=2)
vertical_lines = horizontal_lines.transpose((1, 0, 2))

ax.add_collection(LineCollection(horizontal_lines))
ax.add_collection(LineCollection(vertical_lines))
ax.autoscale()

plt.show()

