import pathlib
import pickle

import ipdb
import pandas as pd


def main():
    csv_dir = pathlib.Path("csv")
    csv_dir.mkdir(exist_ok=True, parents=True)

    # Read times and lengths.
    files = [
        "time_srcs_to_dests.pkl",
        "length_srcs_to_dests.pkl",
        "time_dests_to_dests.pkl",
        "length_dests_to_dests.pkl",
    ]
    for file in files:
        with open(file, "rb") as f:
            arr = pickle.load(f)

        csv_path = csv_dir / pathlib.Path(file).with_suffix(".csv")
        pd.DataFrame(arr).to_csv(csv_path, header=False, index=False)


if __name__ == "__main__":
    with ipdb.launch_ipdb_on_exception():
        main()
