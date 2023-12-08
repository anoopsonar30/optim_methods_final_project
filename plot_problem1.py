import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_floorplan_figure, get_floorplan_image, get_src_dst_scaled, load_gcs_trajs, get_wall_figure


def main():
    srcs, dsts = get_src_dst_scaled()

    trajs_s2d, trajs_d2d = load_gcs_trajs()

    sol_time_npz = np.load("sols/problem1_time.npz")
    sol_dist_npz = np.load("sols/problem1_dist.npz")

    sol_time = sol_time_npz["x"]
    sol_dist = sol_dist_npz["x"]

    print(sol_time)
    print(sol_dist)

    plot_dir = pathlib.Path("plots/problem1")
    plot_dir.mkdir(exist_ok=True, parents=True)

    # fig, ax = get_floorplan_figure()
    fig, ax = get_wall_figure()
    for ii, src in enumerate(srcs):
        for jj, dst in enumerate(dsts):
            if sol_time[ii, jj] > 0.0:
                # ax.plot([src[0], dst[0]], [src[1], dst[1]], color="C1", alpha=0.8)
                traj = trajs_s2d[(ii, jj)]
                ax.plot(traj[:, 0], traj[:, 1], color="C1", alpha=0.8)
    fig.savefig(plot_dir / "p1_min_time.pdf")
    plt.close(fig)

    fig, ax = get_floorplan_figure()
    fig, ax = get_wall_figure()
    for ii, src in enumerate(srcs):
        for jj, dst in enumerate(dsts):
            if sol_dist[ii, jj] > 0.0:
                # ax.plot([src[0], dst[0]], [src[1], dst[1]], color="C1", alpha=0.8)
                traj = trajs_s2d[(ii, jj)]
                ax.plot(traj[:, 0], traj[:, 1], color="C1", alpha=0.8)
    fig.savefig(plot_dir / "p1_min_dist.pdf")
    plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
