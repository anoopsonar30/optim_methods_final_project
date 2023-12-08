import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_src_dst_scaled, get_wall_figure, load_gcs_trajs


def main():
    plot_dir = pathlib.Path("plots/problem3")
    plot_dir.mkdir(exist_ok=True, parents=True)

    srcs, dsts = get_src_dst_scaled()
    trajs_s2d, trajs_d2d = load_gcs_trajs()

    n_src, n_dst = len(srcs), len(dsts)

    sol_time_npz = np.load("sols/problem3_time.npz")
    sol_dist_npz = np.load("sols/problem3_dist.npz")

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist")]:
        x0 = npz["x0"]
        x1 = npz["x1"]

        n_d2d = len(x1)

        fig, ax = get_wall_figure(dpi=500)

        # Plot from src -> dst.
        for ii in range(n_src):
            for jj in range(n_dst):
                if x0[ii, jj] > 0.0:
                    traj = trajs_s2d[(ii, jj)]
                    ax.plot(traj[:, 0], traj[:, 1], color="C1", alpha=0.8)

        # Plot from dst -> dst.
        for kk in range(n_d2d):
            for ii in range(n_dst):
                for jj in range(n_dst):
                    if x1[kk, ii, jj] > 0.0:
                        if ii == jj:
                            continue
                            
                        color = "C{}".format(kk + 2)

                        traj = trajs_d2d[(ii, jj)]
                        if len(traj) > 0:
                            ax.plot(traj[:, 0], traj[:, 1], color=color, alpha=0.8)
                        else:
                            print("No traj for {} -> {}!".format(ii, jj))
                            src, dst = dsts[ii], dsts[jj]
                            ax.plot([src[0], dst[0]], [src[1], dst[1]], color=color, alpha=0.8)

        fig.savefig(plot_dir / f"p3_min_{label}.pdf", bbox_inches="tight")
        fig.savefig(plot_dir / f"p3_min_{label}.png", bbox_inches="tight")
        plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
