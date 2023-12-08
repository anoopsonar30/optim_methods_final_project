import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_floorplan_figure, get_floorplan_image, get_src_dst_scaled


def main():
    image = get_floorplan_image()
    srcs, dsts = get_src_dst_scaled()

    sol_time = np.load("sols/problem1_time.npy")
    sol_dist = np.load("sols/problem1_dist.npy")

    print(sol_time)
    print(sol_dist)

    plot_dir = pathlib.Path("plots/problem1")
    plot_dir.mkdir(exist_ok=True, parents=True)

    fig, ax = get_floorplan_figure()
    for ii, src in enumerate(srcs):
        for jj, dst in enumerate(dsts):
            if sol_time[ii, jj] > 0.0:
                ax.plot([src[0], dst[0]], [src[1], dst[1]], color="C1", alpha=0.8)
    fig.savefig(plot_dir / "p1_min_time.pdf")
    plt.close(fig)

    fig, ax = get_floorplan_figure()
    for ii, src in enumerate(srcs):
        for jj, dst in enumerate(dsts):
            if sol_dist[ii, jj] > 0.0:
                ax.plot([src[0], dst[0]], [src[1], dst[1]], color="C1", alpha=0.8)
    fig.savefig(plot_dir / "p1_min_dist.pdf")
    plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
