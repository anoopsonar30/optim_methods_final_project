import pickle

import ipdb
import matplotlib.pyplot as plt
import numpy as np
import tqdm
from matplotlib.collections import LineCollection, PatchCollection
from pydrake.geometry.optimization import HPolyhedron, Iris, IrisOptions, VPolytope
from scipy.spatial import ConvexHull

from floorplan import get_floorplan_image, get_lines, get_rects, get_seed_points


def main():
    with open("iris_polygons.pkl", "rb") as f:
        free_polys = pickle.load(f)
    with open("iris_polygons2.pkl", "rb") as f:
        free_polys2 = pickle.load(f)
    free_polys = free_polys + free_polys2

    image = get_floorplan_image()
    lines = get_lines()
    rects = get_rects()

    # 105 -> [3.489958, 2.697444]
    # [3.881697, 1.682553]
    # [3.356850, 1.679358]

    seed_points = get_seed_points()

    scale = 1e3
    lines = lines / scale
    rects = rects / scale
    seed_points = seed_points / scale
    imshow_extent = np.array([-0.5, image.width - 0.5, image.height - 0.5, -0.5])
    imshow_extent = imshow_extent / scale

    fig, ax = plt.subplots(figsize=(12, 10), layout="constrained")
    ax.imshow(image, extent=imshow_extent, alpha=0.5, zorder=3)
    col = LineCollection(lines, linewidth=0.2, color="C0", zorder=5)
    ax.add_collection(col)

    seed_patches = []
    for seed_pt in seed_points:
        seed_patches.append(plt.Circle(seed_pt, radius=0.02, facecolor="C6"))
    seed_col = PatchCollection(seed_patches, zorder=6, picker=True, match_original=True)
    ax.add_collection(seed_col)

    # ax.scatter(seed_points[:, 0], seed_points[:, 1], color="C6", zorder=6, pickradius=5)

    patches = []
    for free_poly in free_polys:
        patches.append(plt.Polygon(free_poly, closed=True))
    col = PatchCollection(patches, facecolor="C5", alpha=0.6, zorder=4)
    ax.add_collection(col)

    def onpick(event):
        ind = event.ind[0]
        print(ind)
        print(seed_points[ind])
        print(free_polys[ind])

        nonlocal seed_col
        seed_patches[ind].set_facecolor("C0")
        fig.canvas.draw()

    def onclick(event):
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              (event.button, event.x, event.y, event.xdata, event.ydata))
        circ = plt.Circle((event.xdata, event.ydata), radius=0.02, facecolor="C0", zorder=10)
        ax.add_patch(circ)
        # plt.plot(event.xdata, event.ydata, ',')
        fig.canvas.draw()

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
