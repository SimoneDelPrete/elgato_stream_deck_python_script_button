from os import system


def main():
    if (
        system("xdotool search --desktop 0 --class libreoffice-writer windowactivate")
        != 0
    ):
        system("libreoffice")


if __name__ == "__main__":
    main()
