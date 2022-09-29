from os import system
from subprocess import run


def main():
    if (
        system(
            "xdotool search --desktop 0 --class 'MATLAB R2022b - academic use' windowactivate"
        )
        != 0
    ):
        system("gnome-terminal -e 'bash -c \"matlab ~ & ; bash\" '")


if __name__ == "__main__":
    main()
