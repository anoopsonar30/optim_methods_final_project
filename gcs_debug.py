import pathlib
import pickle
import time

import ipdb
import numpy as np
import tqdm
from pydrake.geometry.optimization import GraphOfConvexSetsOptions, Point, VPolytope
from pydrake.planning import GcsTrajectoryOptimization
from pydrake.solvers import MosekSolver

from floorplan import get_dests, get_sources, get_src_dst_scaled


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
    convex_sets = get_convex_sets()

    srcs, dsts = get_src_dst_scaled()
    source = dsts[6]
    destination = dsts[5]

    #############################################################################
    print("1")
    gcs = GcsTrajectoryOptimization(2)

    print("2")
    regions = gcs.AddRegions(regions=convex_sets, order=3)

    print("3")
    source = gcs.AddRegions([Point(source)], order=0)
    target = gcs.AddRegions([Point(destination)], order=0)
    gcs.AddEdges(source, regions)
    gcs.AddEdges(regions, target)

    print("4")
    gcs.AddTimeCost()
    gcs.AddPathLengthCost()
    gcs.AddVelocityBounds(lb=np.array([-0.1, -0.1]), ub=np.array([0.1, 0.1]))

    print("5")
    options = GraphOfConvexSetsOptions()
    options.preprocessing = True
    options.max_rounded_paths = 50
    start_time = time.time()
    print("Solving GCS...")
    traj, result = gcs.SolvePath(source, target, options)
    print(f"GCS solved in {time.time() - start_time} seconds")
    if not result.is_success():
        print("Could not find a feasible path from source to destination")
        ipdb.set_trace()

    dt = 0.1
    discr_traj = discretize_traj(traj, dt)

    path = pathlib.Path("traj_fixes")
    npy_path = path / "traj56.npy"
    np.save(npy_path, discr_traj)

    print("Saved to {}".format(npy_path))


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
