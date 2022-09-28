from os import system


def main():
    if system("xdotool search --desktop 0 --class Vinagre windowactivate") != 0:
        system("vinagre")


if __name__ == "__main__":
    main()
