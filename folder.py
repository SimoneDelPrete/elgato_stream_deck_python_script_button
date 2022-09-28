from os import system


def main():
    if (
        system("xdotool search --desktop 0 --class Org.gnome.Nautilus windowactivate")
        != 0
    ):
        system("nautilus")


if __name__ == "__main__":
    main()
