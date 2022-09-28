from os import system


def main():
    if system("xdotool search --desktop 0 --class Brave-browser windowactivate") != 0:
        system("brave-browser")


if __name__ == "__main__":
    main()
