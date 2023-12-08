import pickle

import numpy as np


def main():
    traj65 = np.load("traj_fixes/traj56.npy")
    print(traj65.shape)

    with open("data_bk.pkl", "rb") as f:
        s2d_data, d2d_data = pickle.load(f)
    time_srcs_to_dests, length_srcs_to_dests, trajs_s2d = s2d_data
    time_dests_to_dests, length_dests_to_dests, trajs_d2d = d2d_data

    # print(trajs_d2d[(5, 6)])
    a = trajs_d2d[(6, 5)]
    assert len(a) == 0

    trajs_d2d[(6, 5)] = traj65

    # Re-save it.
    d2d_data = time_dests_to_dests, length_dests_to_dests, trajs_d2d
    data = [s2d_data, d2d_data]

    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    print("Saved fixed data to data.pkl!")


if __name__ == "__main__":
    main()
