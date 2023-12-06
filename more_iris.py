import pickle

import ipdb
import matplotlib.pyplot as plt
import numpy as np
import tqdm
from matplotlib.collections import LineCollection, PatchCollection
from pydrake.geometry.optimization import HPolyhedron, Iris, IrisOptions, VPolytope
from scipy.spatial import ConvexHull

from floorplan import get_floorplan_image, get_lines, get_rects, get_seed_points, get_seed_points2


def main():
    image = get_floorplan_image()
    lines = get_lines()
    rects = get_rects()

    seed_points2 = get_seed_points2()

    scale = 1e3
    lines = lines / scale
    rects = rects / scale
    seed_points2 = seed_points2 / scale
    imshow_extent = np.array([-0.5, image.width - 0.5, image.height - 0.5, -0.5])
    imshow_extent = imshow_extent / scale

    fig, ax = plt.subplots(figsize=(12, 10), layout="constrained")
    ax.imshow(image, extent=imshow_extent, alpha=0.5, zorder=3)
    col = LineCollection(lines, linewidth=0.2, color="C0", zorder=5)
    ax.add_collection(col)

    # Get obstacles for IRIS
    obstacles = []
    for rect in rects:
        # VPolytope needs (2, n_points).
        obstacles.append(VPolytope(rect.T))

    domain = HPolyhedron.MakeBox([0, 0], [image.width / scale, image.height / scale])

    # Run IRIS.
    iris_options = IrisOptions()
    iris_options.iteration_limit = 10

    # Run IRIS.
    iris_options = IrisOptions()
    iris_options.iteration_limit = 10

    free_polys2 = []
    for seed_point in tqdm.tqdm(seed_points2):
        assert seed_point.shape == (2,)
        free_hpoly = Iris(obstacles, seed_point, domain, iris_options)
        free_vpoly = VPolytope(free_hpoly)

        # Compute convex hull as way to get vertices in order.
        free_poly_verts = free_vpoly.vertices().T
        argsort = ConvexHull(free_poly_verts).vertices
        free_poly_verts = free_poly_verts[argsort]
        free_polys2.append(free_poly_verts)

    with open("iris_polygons.pkl", "rb") as f:
        free_polys = pickle.load(f)

    del free_polys[105]
    patches = []
    for free_poly in free_polys:
        patches.append(plt.Polygon(free_poly, closed=True))
    col = PatchCollection(patches, facecolor="C5", alpha=0.6, zorder=4)
    ax.add_collection(col)

    patches = []
    for free_poly in free_polys2:
        patches.append(plt.Polygon(free_poly, closed=True))
    col = PatchCollection(patches, facecolor="C4", alpha=0.6, zorder=4.5)
    ax.add_collection(col)
    fig.savefig("floorplan_iris2.pdf")

    # Save the iris polygons.
    with open("iris_polygons2.pkl", "wb") as f:
        pickle.dump(free_polys2, f)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
