"""
    Module clicker: when the user presses "s" module makes 10 clicks per seconds.
    To stop you need to press "s" again.
"""
from pynput.mouse import Controller, Button
import keyboard
import time

MOUSE = Controller()
AUTOCLICK: bool = False


def clicker() -> None:
    """
    A function that makes clicks if the user has started the process

    return: None
    """
    while True:
        if AUTOCLICK:
            MOUSE.click(Button.left)
            time.sleep(0.1)


def check_keyboards() -> None:
    """
    A function that controls pressing "s" and changes flag if "s" has been pressed

    return: None
    """
    global AUTOCLICK
    while True:
        if keyboard.read_key() == "s":
            AUTOCLICK = not AUTOCLICK



def main():
    check_keyboards()


if __name__ == "__main__":
    main()
