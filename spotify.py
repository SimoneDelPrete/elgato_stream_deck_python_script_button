from os import system


def main():
    if system("xdotool search --desktop 0 --class Spotify windowactivate") != 0:
        system("spotify")


if __name__ == "__main__":
    main()
