from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Listener
import threading
import time
import random

mouse_controller = MouseController()

toggled = set()

class Clicker:
    def __init__(
        self,
        master = '`',
        left = 'f',
        right = 'c'
    ):
        self.key_map = {
            "master": master.lower(),
            "left": left.lower(),
            "right": right.lower()
        }
        self.char_to_name = {v: k for k, v in self.key_map.items()}

        threading.Thread(target=self.clicker, daemon=True).start()

        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
    
    def clicker(self):
        while True:
            if "master" in toggled:
                # Left clicker
                if "left" in toggled:
                    mouse_controller.press(Button.left)
                    time.sleep(random.uniform(0.03, 0.05))
                    mouse_controller.release(Button.left)
                    time.sleep(random.uniform(0.04, 0.08))

                # Right clicker
                if "right" in toggled:
                    mouse_controller.press(Button.right)
                    time.sleep(random.uniform(0.03, 0.05))
                    mouse_controller.release(Button.right)
                    time.sleep(random.uniform(0.04, 0.08))
            else:
                time.sleep(0.05)
            

    def on_press(self, key):
        try:
            if hasattr(key, "char") and key.char is not None:
                ch = key.char.lower()
                if ch in self.char_to_name:
                    name = self.char_to_name[ch]
                    if name in toggled:
                        toggled.remove(name)
                    else:
                        toggled.add(name)
                    
                    if name == "master":
                        toggled.discard("left")
                        toggled.discard("right")
        except AttributeError:
            pass

if __name__ == "__main__":
    Clicker()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
