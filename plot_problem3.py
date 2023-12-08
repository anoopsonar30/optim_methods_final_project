import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_src_dst_scaled, get_wall_figure, load_gcs_trajs, load_time_and_dist


def main():
    plot_dir = pathlib.Path("plots/problem3")
    plot_dir.mkdir(exist_ok=True, parents=True)

    srcs, dsts = get_src_dst_scaled()
    trajs_s2d, trajs_d2d = load_gcs_trajs()

    # (n_src, n_dst)
    # (n_src, n_dst)
    # (n_dst, n_dst)
    # (n_dst, n_dst)
    T_s2d, L_s2d, T_d2d, L_d2d = load_time_and_dist()

    n_src, n_dst = len(srcs), len(dsts)

    sol_time_npz = np.load("sols/problem3_time.npz")
    sol_dist_npz = np.load("sols/problem3_dist.npz")

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist")]:
        x0 = npz["x0"]
        # (n_d2d, n_dest, n_dest)
        x1 = npz["x1"]

        # Compute the total time and total distance.
        total_time0 = np.sum(T_s2d * x0)
        total_time1 = np.sum(T_d2d * x1)
        total_time = total_time0 + total_time1

        total_dist0 = np.sum(L_s2d * x0)
        total_dist1 = np.sum(L_d2d * x1)
        total_dist = total_dist0 + total_dist1

        n_d2d = len(x1)

        colors = ["C2", "C4", "C5"]

        fig, ax = get_wall_figure(dpi=500)

        dst_idx = np.full(n_dst, 100, dtype=np.int32)

        # Plot from src -> dst.
        for ii in range(n_src):
            for jj in range(n_dst):
                if x0[ii, jj] > 0.0:
                    dst_idx[jj] = ii
                    color = colors[ii]

                    traj = trajs_s2d[(ii, jj)]
                    ax.plot(traj[:, 0], traj[:, 1], color=color, alpha=0.8)

        # Plot from dst -> dst.
        for kk in range(n_d2d):
            # We are moving in time.
            for ii in range(n_dst):
                for jj in range(n_dst):
                    if x1[kk, ii, jj] > 0.0:
                        if ii == jj:
                            continue

                        # We have moved from ii -> jj. Update the dst_idx.
                        dst_idx[jj] = dst_idx[ii]
                        color = colors[dst_idx[ii]]
                        dst_idx[ii] = 100

                        traj = trajs_d2d[(ii, jj)]
                        if len(traj) > 0:
                            ax.plot(traj[:, 0], traj[:, 1], color=color, alpha=0.8)
                        else:
                            print("No traj for {} -> {}!".format(ii, jj))
                            src, dst = dsts[ii], dsts[jj]
                            ax.plot([src[0], dst[0]], [src[1], dst[1]], color=color, alpha=0.8)

        ax.set_title("Time: {:.2f} s    Dist: {:.2f} m".format(total_time, total_dist))
        fig.savefig(plot_dir / f"p3_min_{label}.pdf", bbox_inches="tight")
        fig.savefig(plot_dir / f"p3_min_{label}.png", bbox_inches="tight")
        plt.close(fig)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
