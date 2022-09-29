from os import system


def main():
    if system('xdotool search --desktop 0 --class "microsoft Teams - Preview"') != 0:
        system("teams")


if __name__ == "__main__":
    main()
