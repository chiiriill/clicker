"""
    Module clicker: when the user presses "s" module makes 10 clicks per seconds.
    To stop you need to press "s" again.
"""
from pynput.mouse import Controller, Button
import time

MOUSE = Controller()
CLICK: bool = False


def clicker() -> None:
    """
    A function that makes clicks if the user has started the process

    return: None
    """
    while True:
        if CLICK:
            MOUSE.click(Button.left)
            time.sleep(0.1)


def main():
    pass


if __name__ == "__main__":
    main()
