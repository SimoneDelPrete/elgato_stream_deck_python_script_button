from os import system


def main():
    if system("xdotool search --desktop 0 --class Evince windowactivate") != 0:
        system("evince")


if __name__ == "__main__":
    main()
