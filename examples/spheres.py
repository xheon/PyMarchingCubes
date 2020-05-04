
import numpy as np
import marching_cubes as mcubes

print("Example 1: Isosurface in NumPy volume...")
#print(mcubes.__dir__())

# Create a data volume (100 x 100 x 100)
X, Y, Z = np.mgrid[:100, :100, :100]
sdf = (X-50)**2 + (Y-50)**2 + (Z-50)**2 - 25**2

# Extract the 0-isosurface
vertices, triangles = mcubes.marching_cubes(sdf, 0)
mcubes.export_obj(vertices, triangles, "sphere.obj")




print("Example 2: Isosurface and color in NumPy volume...")

# Extract isosurface and color
color = 0.01 * np.concatenate((X[:,:,:,None],X[:,:,:,None],X[:,:,:,None]), axis=3) # color array (grayscale gradient in this example)
vertices_color, triangles_color = mcubes.marching_cubes_color(sdf, color, 0)
mcubes.export_obj(vertices_color, triangles_color, "sphere_color.obj")
mcubes.export_off(vertices_color, triangles_color, "sphere_color.off")






# old examples

# Export the result to sphere.dae
#mcubes.export_mesh(vertices1, triangles1, "sphere1.dae", "MySphere")

# print("Done. Result saved in 'sphere1.dae'.")

# print("Example 2: Isosurface in Python function...")
# print("(this might take a while...)")

# # Create the volume
# def f(x, y, z):
#     return x**2 + y**2 + z**2

# # Extract the 16-isosurface
# vertices2, triangles2 = mcubes.marching_cubes_func(
#         (-10,-10,-10), (10,10,10),  # Bounds
#         100, 100, 100,              # Number of samples in each dimension
#         f,                          # Implicit function
#         16)                         # Isosurface value

# # Export the result to sphere2.dae
# mcubes.export_mesh(vertices2, triangles2, "sphere2.dae", "MySphere")
# print("Done. Result saved in 'sphere2.dae'.")

# try:
#     print("Plotting mesh...")
#     from mayavi import mlab
#     mlab.triangular_mesh(
#         vertices1[:, 0], vertices1[:, 1], vertices1[:, 2],
#         triangles1)
#     print("Done.")
#     mlab.show()
# except ImportError:
#     print("Could not import mayavi. Interactive demo not available.")
