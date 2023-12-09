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
    sol_l2_npz = np.load("sols/problem3_l2dist.npz")

    ts = []
    ds = []

    for npz, label in [(sol_time_npz, "time"), (sol_dist_npz, "dist"), (sol_l2_npz, "l2dist")]:
        # (n_dest, n_dest)
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

        n_robots_tmp = 0
        rbt_idx = np.full(n_dst, 100, dtype=np.int32)
        dst_idx = np.full(n_dst, 100, dtype=np.int32)

        n_robots = int(np.round(x0.sum()))
        robot_times = np.zeros(n_robots)
        robot_dists = np.zeros(n_robots)

        # Plot from src -> dst.
        for ii in range(n_src):
            for jj in range(n_dst):
                if x0[ii, jj] > 0.0:
                    dst_idx[jj] = ii
                    rbt_idx[jj] = n_robots_tmp
                    n_robots_tmp += 1
                    color = colors[ii]

                    robot_times[rbt_idx[jj]] += T_s2d[ii, jj]
                    robot_dists[rbt_idx[jj]] += L_s2d[ii, jj]

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
                        rbt_idx[jj] = rbt_idx[ii]

                        color = colors[dst_idx[ii]]
                        rbt_idx[ii] = 100
                        dst_idx[ii] = 100

                        robot_times[rbt_idx[jj]] += T_d2d[ii, jj]
                        robot_dists[rbt_idx[jj]] += L_d2d[ii, jj]

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

        ts.append(total_time)
        ds.append(total_dist)

        robot_times = np.sort(np.array(robot_times))
        robot_dists = np.sort(np.array(robot_dists))
        times_str = ", ".join(["{:.2f}".format(tt) for tt in np.sort(robot_times)])
        dists_str = ", ".join(["{:.2f}".format(tt) for tt in np.sort(robot_dists)])
        print("Times: {}, Dists: {}".format(times_str, dists_str))

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
