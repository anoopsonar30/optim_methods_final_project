import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_src_dst_scaled, get_wall_figure, load_gcs_trajs, load_time_and_dist


def main():
    plot_dir = pathlib.Path("plots/problem1")
    plot_dir.mkdir(exist_ok=True, parents=True)

    srcs, dsts = get_src_dst_scaled()
    trajs_s2d, trajs_d2d = load_gcs_trajs()

    # (n_src, n_dst)
    # (n_src, n_dst)
    # (n_dst, n_dst)
    # (n_dst, n_dst)
    T_s2d, L_s2d, T_d2d, L_d2d = load_time_and_dist()

    n_src, n_dst = len(srcs), len(dsts)

    sol_time_npz = np.load("sols/problem1_time.npz")
    sol_dist_npz = np.load("sols/problem1_dist.npz")

    colors = ["C2", "C4", "C5"]

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist")]:
        # (n_src, n_dst)
        x = npz["x"]

        # Compute the total time and total distance.
        total_time = np.sum(T_s2d * x)
        total_dist = np.sum(L_s2d * x)

        fig, ax = get_wall_figure(dpi=500)

        # Plot from src -> dst.
        for ii in range(n_src):
            for jj in range(n_dst):
                if x[ii, jj] > 0.0:
                    # ls = linestyles[ii]
                    color = colors[ii]
                    traj = trajs_s2d[(ii, jj)]
                    ax.plot(traj[:, 0], traj[:, 1], color=color, alpha=0.8)

        ax.set_title("Time: {:.2f} s    Dist: {:.2f} m".format(total_time, total_dist))
        fig.savefig(plot_dir / f"p1_min_{label}.pdf", bbox_inches="tight")
        fig.savefig(plot_dir / f"p1_min_{label}.png", bbox_inches="tight")
        plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
