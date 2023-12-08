import pickle
import time

import ipdb
import numpy as np
import tqdm
from pydrake.geometry.optimization import GraphOfConvexSetsOptions, Point, VPolytope
from pydrake.planning import GcsTrajectoryOptimization
from pydrake.solvers import MosekSolver

from floorplan import get_dests, get_sources


# from pydrake.geometry.optimization import HPolyhedron, Iris, IrisOptions, VPolytope


def gcs_traj_opt(source, destination, convex_sets):
    gcs = GcsTrajectoryOptimization(2)

    regions = gcs.AddRegions(regions=convex_sets, order=3)

    source = gcs.AddRegions([Point(source)], order=0)
    target = gcs.AddRegions([Point(destination)], order=0)
    gcs.AddEdges(source, regions)
    gcs.AddEdges(regions, target)

    gcs.AddTimeCost()
    gcs.AddPathLengthCost()
    gcs.AddVelocityBounds(lb=np.array([-0.1, -0.1]), ub=np.array([0.1, 0.1]))

    options = GraphOfConvexSetsOptions()
    options.preprocessing = True
    options.max_rounded_paths = 20
    start_time = time.time()
    print("Solving GCS...")
    traj, result = gcs.SolvePath(source, target, options)
    print(f"GCS solved in {time.time() - start_time} seconds")
    if not result.is_success():
        raise ValueError("Could not find a feasible path from source to destination")

    return traj


def get_traj_duration(traj):
    return traj.end_time() - traj.start_time()


def get_traj_length(traj):
    step_size = 0.1
    timestamps = np.arange(traj.start_time(), traj.end_time(), step_size)

    pos = []
    for t in timestamps:
        pos.append(traj.value(t).reshape(1, 2)[0])
    pos = np.array(pos)

    path_length = 0
    for t in range(len(pos) - 1):
        path_length += np.linalg.norm(pos[t + 1] - pos[t])

    return path_length


def get_convex_sets():
    with open("iris_polygons3.pkl", "rb") as f:
        free_polys = pickle.load(f)

    convex_sets = []
    for free_poly in free_polys:
        convex_sets.append(VPolytope(free_poly.T))
    return convex_sets


def discretize_traj(traj, dt: float):
    num = int((traj.end_time() - traj.start_time()) / dt)
    timestamps = np.linspace(traj.start_time(), traj.end_time(), num=num)

    T_pos = []
    for tt in timestamps:
        T_pos.append(traj.value(tt).reshape(1, 2)[0])
    T_pos = np.stack(T_pos, axis=0)
    return T_pos


def main():
    assert MosekSolver().enabled()

    scale = 1e3
    srcs = get_sources() / scale
    dests = get_dests() / scale
    print("n_srcs: {}, n_dsts: {}".format(len(srcs), len(dests)))

    print("Getting convex sets...")
    convex_sets = get_convex_sets()
    print("Getting convex sets... Done!")

    dt = 0.1

    time_srcs_to_dests = np.zeros((len(srcs), len(dests)))
    length_srcs_to_dests = np.zeros((len(srcs), len(dests)))
    trajs_s2d = {}
    for ii, src in enumerate(tqdm.tqdm(srcs, position=0)):
        for jj, dst in enumerate(tqdm.tqdm(dests, position=1)):
            traj = gcs_traj_opt(src, dst, convex_sets)
            time_srcs_to_dests[ii][jj] = get_traj_duration(traj)
            length_srcs_to_dests[ii][jj] = get_traj_length(traj)
            trajs_s2d[(ii, jj)] = discretize_traj(traj, dt)

    time_dests_to_dests = np.zeros((len(dests), len(dests)))
    length_dests_to_dests = np.zeros((len(dests), len(dests)))
    trajs_d2d = {}
    for ii, dst_1 in enumerate(tqdm.tqdm(dests, position=0)):
        for jj, dst_2 in enumerate(tqdm.tqdm(dests, position=1)):
            try:
                traj = gcs_traj_opt(dst_1, dst_2, convex_sets)

                if ii == jj:
                    time_dests_to_dests[ii][jj] = 0.0
                    length_dests_to_dests[ii][jj] = 0.0
                    trajs_d2d[(ii, jj)] = np.zeros((0, 2))
                else:
                    time_dests_to_dests[ii][jj] = get_traj_duration(traj)
                    length_dests_to_dests[ii][jj] = get_traj_length(traj)
                    trajs_d2d[(ii, jj)] = discretize_traj(traj, dt)
            except ValueError as e:
                print(e)
                time_dests_to_dests[ii][jj] = -1.0
                length_dests_to_dests[ii][jj] = -1.0
                trajs_d2d[(ii, jj)] = np.zeros((0, 2))

    # Save.
    s2d_data = [time_srcs_to_dests, length_srcs_to_dests, trajs_s2d]
    d2d_data = [time_dests_to_dests, length_dests_to_dests, trajs_d2d]
    data = [s2d_data, d2d_data]
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    print("Saved data to data.pkl!")


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
