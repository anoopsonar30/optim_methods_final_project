import pathlib

import ipdb
import numpy as np
import pandas as pd

from floorplan import get_src_dst_scaled


def main():
    srcs, dsts = get_src_dst_scaled()

    # Compute the Euclidean distance between each source and destination.
    # (n_src, n_dst)
    dists_s2d = np.linalg.norm(srcs[:, None, :] - dsts[None, :, :], axis=2)
    # (n_dst, n_dst)
    dists_d2d = np.linalg.norm(dsts[:, None, :] - dsts[None, :, :], axis=2)

    # Save as csv.
    csv_dir = pathlib.Path("csv")
    csv_dir.mkdir(exist_ok=True, parents=True)

    pd.DataFrame(dists_s2d).to_csv(csv_dir / "l2_s2d.csv", header=False, index=False)
    pd.DataFrame(dists_d2d).to_csv(csv_dir / "l2_d2d.csv", header=False, index=False)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
