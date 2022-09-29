from os import system


def main():
    if (
        system(
            "xdotool search --desktop 0 --class 'MATLAB R2022b - academic use' windowactivate"
        )
        != 0
    ):
        system('gnome-terminal --tab --active -- bash -c "cd ~; matlab ; exec bash"')


if __name__ == "__main__":
    main()
