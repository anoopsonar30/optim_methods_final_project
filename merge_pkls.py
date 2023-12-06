import pickle


def main():
    with open("iris_polygons.pkl", "rb") as f:
        free_polys = pickle.load(f)

    with open("iris_polygons2.pkl", "rb") as f:
        free_polys2 = pickle.load(f)

    free_polys = free_polys + free_polys2
    with open("iris_polygons3.pkl", "wb") as f:
        pickle.dump(free_polys, f)

    print("Total of {} polygons!".format(len(free_polys)))


if __name__ == "__main__":
    main()
