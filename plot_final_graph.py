import pickle

import ipdb
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection, PatchCollection

from floorplan import get_dests, get_floorplan_image, get_lines, get_rects, get_sources


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

    fig.savefig("floorplan_final.pdf")


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
