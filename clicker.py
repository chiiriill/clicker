"""
    Module clicker: when the user presses "s" module makes 10 clicks per seconds.
    To stop you need to press "s" again.
"""
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import threading
import time
import os

MOUSE = Controller()
AUTOCLICK: bool = False
START_KEY = KeyCode(char="s")
END_KEY = KeyCode(char="q")


def clicker() -> None:
    """
    A function that makes clicks if the user has started the process

    return: None
    """
    while True:
        if AUTOCLICK:
            MOUSE.click(Button.left)
            time.sleep(0.1)


def check_keyboards(key) -> None:
    """
    A function that controls pressing "s" and changes flag if "s" has been pressed

    return: None
    """
    global AUTOCLICK
    if key == START_KEY:
        AUTOCLICK = not AUTOCLICK
    elif key == END_KEY:
        os.abort()


def main():
    """Main function """
    clicking = threading.Thread(target=clicker)
    clicking.start()

    with Listener(on_press=check_keyboards) as listener:
        listener.join()


if __name__ == "__main__":
    main()
