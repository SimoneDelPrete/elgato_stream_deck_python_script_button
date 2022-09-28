from os import system


def main():
    if system("xdotool search --desktop 0 --class 'Microsoft Teams - Preview'") != 0:
        system("teams")


if __name__ == "__main__":
    main()
