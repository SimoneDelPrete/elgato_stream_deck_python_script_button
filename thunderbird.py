from os import system


def main():
    if system("xdotool search --desktop 0 --class Thunderbird windowactivate") != 0:
        system("thunderbird")


if __name__ == "__main__":
    main()
