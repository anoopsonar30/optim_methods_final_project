import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_src_dst_scaled, get_wall_figure, load_gcs_trajs


def main():
    plot_dir = pathlib.Path("plots/problem2")
    plot_dir.mkdir(exist_ok=True, parents=True)

    srcs, dsts = get_src_dst_scaled()
    trajs_s2d, trajs_d2d = load_gcs_trajs()

    n_src, n_dst = len(srcs), len(dsts)

    sol_time_npz = np.load("sols/problem2_time.npz")
    sol_dist_npz = np.load("sols/problem2_dist.npz")

    linestyles = ["-", "--", ":"]

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist")]:
        x = npz["x"]

        fig, ax = get_wall_figure(dpi=500)

        # Plot from src -> dst.
        for ii in range(n_src):
            for jj in range(n_dst):
                if x[ii, jj] > 0.0:
                    # ls = linestyles[ii]
                    color = f"C{ii + 2}"
                    traj = trajs_s2d[(ii, jj)]
                    ax.plot(traj[:, 0], traj[:, 1], color=color, alpha=0.8)

        fig.savefig(plot_dir / f"p2_min_{label}.pdf", bbox_inches="tight")
        fig.savefig(plot_dir / f"p2_min_{label}.png", bbox_inches="tight")
        plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
