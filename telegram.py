from os import system


def main():
    if system("xdotool search --desktop 0 --class TelegramDesktop windowactivate") != 0:
        system("~/.Telegram/Telegram")


if __name__ == "__main__":
    main()
