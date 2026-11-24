import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w") as f:
        f.write("158\n")


if __name__ == "__main__":
    main()
