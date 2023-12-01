import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

from pydrake.geometry.optimization import Iris
from pydrake.geometry.optimization import VPolytope
from pydrake.geometry.optimization import HPolyhedron

# Set the domain space within which we will operate
domain = HPolyhedron.MakeBox([0, 0], [100, 100])

# Create an empty list of obstacles
obstacles = []

# Add two vertical walls at x = 20 and x = 80
obstacles.append(VPolytope(np.array(([19.9, 19.9, 20.1, 20.1], [0, 100, 100, 0]))))
obstacles.append(VPolytope(np.array(([80, 80, 80.2, 80.2], [0, 100, 100, 0]))))

# print(obstacles[0].vertices())
# print(obstacles[0].ambient_dimension())

# Set an initial seed point to (50, 50)
seed_point = [50, 50]

# Create an IRIS region using that seedpoint
free_hpolyhedron = Iris(obstacles, seed_point, domain)

free_vpolytope = VPolytope(free_hpolyhedron)
free_vertices = free_vpolytope.vertices()

# The above vertices are not in clockwise/counterclockwise order so the plot is a little off
# Compute the convex hull and extract the order
plot_order = ConvexHull(free_vertices.T).vertices
plot_free_vertices = [[], []]
for i in range (len(free_vertices[0])):
    ind = np.where(plot_order == i)
    plot_free_vertices[0].append(free_vertices[0][ind])
    plot_free_vertices[1].append(free_vertices[1][ind])

# Set the bound of the figure
plt.figure()
# plt.xlim(0, 100)
# plt.ylim(0, 100)

# Plot the obstacle
for obstacle in obstacles:
    vertices = obstacle.vertices()
    plt.plot(vertices[0], vertices[1])
    
# Plot the IRIS convex polytope as shaded region    
plt.fill(plot_free_vertices[0], plot_free_vertices[1], "brown")

plt.show()