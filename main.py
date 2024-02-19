# Import dependencies
import matplotlib.pyplot as plt
import numpy as np


# Define diagram type and create diagram
ax = plt.axes(projection='3d')

# Create data
x_data = np.linspace(616, 619.5, 8)
y_data = np.linspace(167, 165, 5)
X, Y = np.meshgrid(x_data, y_data)
Z = np.array([
    [1_800, 1_730, 1_580, 1_380, 1_410, 1_030, 820, 695],
    [2_080, 1_990, 1_740, 1_580, 1_300, 1_000, 770, 710],
    [2_190, 2_240, 1_960, 1_580, 1_260, 920, 710, 760],
    [2_020, 1_990, 1_570, 1_340, 1_000, 800, 680, 810],
    [1_670, 1_680, 1_260, 1_030, 780, 670, 750, 830]
])

# Plot the data and show it
ax.plot_surface(X, Y, Z, color="g")
plt.show()
