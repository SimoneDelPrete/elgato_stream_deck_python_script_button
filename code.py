from os import system


def main():
    if system("xdotool search --desktop 0 --class Code windowactivate") != 0:
        system("code")


if __name__ == "__main__":
    main()
