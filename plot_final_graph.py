import pickle
import ipdb
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection

from pydrake.solvers import MathematicalProgram, Solve, MosekSolver
from pydrake.planning import GcsTrajectoryOptimization
from pydrake.geometry.optimization import Point, GraphOfConvexSetsOptions, VPolytope
# from pydrake.geometry.optimization import HPolyhedron, Iris, IrisOptions, VPolytope

from floorplan import get_dests, get_floorplan_image, get_lines, get_rects, get_sources

if MosekSolver().enabled():
    print("It looks like you have a Mosek license")

def main():
    image = get_floorplan_image()
    lines = get_lines()
    rects = get_rects()
    dests = get_dests()
    srcs = get_sources()

    with open("iris_polygons3.pkl", "rb") as f:
        free_polys = pickle.load(f)

    scale = 1e3
    lines = lines / scale
    rects = rects / scale
    dests = dests / scale
    srcs = srcs / scale
    imshow_extent = np.array([-0.5, image.width - 0.5, image.height - 0.5, -0.5])
    imshow_extent = imshow_extent / scale

    fig, ax = plt.subplots(figsize=(12, 10), layout="constrained")
    ax.imshow(image, extent=imshow_extent, alpha=0.5, zorder=3)
    col = LineCollection(lines, linewidth=0.2, color="C0", zorder=5)
    ax.add_collection(col)

    # Plot walls.
    patches = []
    for rect in rects:
        patches.append(plt.Polygon(rect, closed=True))
    col = PatchCollection(patches, facecolor="C3", alpha=0.6, zorder=4)
    ax.add_collection(col)

    # Plot dests.
    ax.scatter(dests[:, 0], dests[:, 1], color="C1", zorder=6)

    # Plot sources.
    ax.scatter(srcs[:, 0], srcs[:, 1], color="C0", zorder=6)

    # Plot iris regions.
    patches = []
    for free_poly in free_polys:
        patches.append(plt.Polygon(free_poly, closed=True))
    col = PatchCollection(patches, facecolor="C5", alpha=0.3, zorder=4)
    ax.add_collection(col)

    gcs = GcsTrajectoryOptimization(2)
    
    convex_sets = []    
    for free_poly in free_polys:
        convex_sets.append(VPolytope(free_poly.T))
    
    regions = gcs.AddRegions(regions=convex_sets, order=3)
    source = gcs.AddRegions([Point(srcs[0, :])], order=0)
    target = gcs.AddRegions([Point(dests[0, :])], order=0)
    
    gcs.AddEdges(source, regions)
    gcs.AddEdges(regions, target)
    
    gcs.AddTimeCost()
    # gcs.AddVelocityBounds(
    #     plant.GetVelocityLowerLimits(), plant.GetVelocityUpperLimits()
    # )

    options = GraphOfConvexSetsOptions()
    options.preprocessing = True
    options.max_rounded_paths = 5
    start_time = time.time()
    traj, result = gcs.SolvePath(source, target, options)
    print(f"GCS solved in {time.time() - start_time} seconds")
    if not result.is_success():
        print("Could not find a feasible path from source to destination")
    
    # fig.savefig("floorplan_final.pdf")


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
