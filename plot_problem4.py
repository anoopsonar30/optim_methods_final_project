import pathlib

import ipdb
import matplotlib.pyplot as plt
import numpy as np

from floorplan import get_src_dst_scaled, get_wall_figure, load_gcs_trajs, load_time_and_dist


def main():
    plot_dir = pathlib.Path("plots/problem4")
    plot_dir.mkdir(exist_ok=True, parents=True)

    srcs, dsts = get_src_dst_scaled()
    trajs_s2d, trajs_d2d = load_gcs_trajs()
    T_s2d, L_s2d, T_d2d, L_d2d = load_time_and_dist()

    n_src, n_dst = len(srcs), len(dsts)

    sol_time_npz = np.load("sols/problem4_time.npz")
    sol_dist_npz = np.load("sols/problem4_dist.npz")
    sol_l2_npz = np.load("sols/problem4_l2dist.npz")

    linestyles = ["-", "--", "-.", ":"]
    colors = ["C2", "C4", "C5", "C6"]

    ts = []
    ds = []

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist"), (sol_l2_npz, "l2dist")]:
        # (n_robot, n_src, n_dst)
        x0 = npz["x0"]
        # (n_robot, n_d2d, n_dst, n_dst)
        x1 = npz["x1"]

        # Sort robot, first by x coordinate of start, then by x coordinates of destination.
        tmp = 10 * np.argmax(x0.sum(axis=2), axis=1) + np.argmax(x0.sum(axis=1), axis=1)
        robot_order = np.argsort(tmp)
        x0 = x0[robot_order]
        x1 = x1[robot_order]

        # Compute the total time and total distance per robot.
        total_time0 = np.sum(T_s2d * x0, axis=(1, 2))
        total_time1 = np.sum(T_d2d * x1, axis=(1, 2, 3))
        total_times = total_time0 + total_time1

        total_dist0 = np.sum(L_s2d * x0, axis=(1, 2))
        total_dist1 = np.sum(L_d2d * x1, axis=(1, 2, 3))
        total_dists = total_dist0 + total_dist1

        ls = "-"

        n_robot, n_d2d, _, _ = x1.shape

        fig, ax = get_wall_figure(dpi=500)

        # Plot from src -> dst.
        for rr in range(n_robot):
            for ii in range(n_src):
                for jj in range(n_dst):
                    if x0[rr, ii, jj] > 0.0:
                        # ls = linestyles[rr]
                        # color = "C1"
                        # ls = "--"
                        color = colors[rr]

                        traj = trajs_s2d[(ii, jj)]
                        ax.plot(traj[:, 0], traj[:, 1], color=color, ls=ls, alpha=0.8)

        # Plot from dst -> dst.
        for rr in range(n_robot):
            for kk in range(n_d2d):
                for ii in range(n_dst):
                    for jj in range(n_dst):
                        if x1[rr, kk, ii, jj] > 0.0:
                            if ii == jj:
                                continue

                            # ls = linestyles[rr]
                            # color = "C{}".format(kk + 2)
                            # ls = "--"
                            color = colors[rr]

                            traj = trajs_d2d[(ii, jj)]
                            if len(traj) > 0:
                                ax.plot(traj[:, 0], traj[:, 1], color=color, ls=ls, alpha=0.8)
                            elif len(traj := trajs_d2d[(jj, ii)]) > 0:
                                ax.plot(traj[:, 0], traj[:, 1], color=color, ls=ls, alpha=0.8)
                            else:
                                ipdb.set_trace()
                                src, dst = dsts[ii], dsts[jj]
                                ax.plot([src[0], dst[0]], [src[1], dst[1]], color=color, ls=ls, alpha=0.8)

        total_times_str = ", ".join(["{:.2f}".format(tt) for tt in np.sort(total_times)])
        total_dists_str = ", ".join(["{:.2f}".format(tt) for tt in np.sort(total_dists)])

        ax.set_title("Time: [{}] s\nDist: [{}] m".format(total_times_str, total_dists_str))
        fig.savefig(plot_dir / f"p4_min_{label}.pdf", bbox_inches="tight", pad_inches=2e-3)
        fig.savefig(plot_dir / f"p4_min_{label}.png", bbox_inches="tight", pad_inches=2e-3)
        plt.close(fig)

        print("Times: {}, Dists: {}".format(total_times_str, total_dists_str))

        ts.append(total_times.max())
        ds.append(total_dists.max())

    # Compute percentage change in time and distance
    t_pct = (ts[0] - ts[1]) / ts[1]
    d_pct = (ds[0] - ds[1]) / ds[1]
    print("[From min distance] Time: {:.3f}%, Distance: {:.3f}%".format(t_pct * 100, d_pct * 100))

    t_pct = (ts[0] - ts[2]) / ts[2]
    d_pct = (ds[0] - ds[2]) / ds[2]
    print("[From min l2] Time: {:.3f}%, Distance: {:.3f}%".format(t_pct * 100, d_pct * 100))


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
