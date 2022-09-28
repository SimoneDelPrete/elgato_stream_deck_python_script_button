from os import system


def main():
    if (
        system(
            "xdotool search --desktop 0 --class 'MATLAB R2022b - academic use' windowactivate"
        )
        != 0
    ):
        system("/usr/local/MATLAB/R2022b/bin/matlab")


if __name__ == "__main__":
    main()
