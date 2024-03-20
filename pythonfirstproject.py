import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-

# Setting coordinates for points on the line
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Plotting the graph with markers and a red line
plt.plot(x, y, marker='o', linestyle='-', color='red', label='Line y=2x')

# Additional plot settings
plt.title('Graph with a line')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()

# Adding the intersection with the line (adding a horizontal line)
plt.axhline(y=4, color='violet', linestyle='-', label='Intersection with y=4')

# Adding a perpendicular to the x-axis from the intersection point with an arrow
plt.annotate('',
             xy=(2, 4),  # coordinates of the arrow end
             xytext=(2, -0.4),  # starting coordinates of the arrow (slightly above the x-axis)
             arrowprops=dict(arrowstyle='-', color='blue', linestyle='--'),  # arrow parameters
             )

# Displaying the graph
plt.show()
