from os import system


def main():
    if system("xdotool search --desktop 0 --class Terminal windowactivate") != 0:
        system("gnome-terminal")


if __name__ == "__main__":
    main()
