from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Listener
import threading
import time
import random

# Mouse controller to perform clicks
mouse_controller = MouseController()

# The global set of toggles
toggled = set()


class Clicker:
    def __init__(
        self,
        master='`',
        left='f',
        right='c'
    ):
        self.key_map = {
            "master": master.lower(),
            "left": left.lower(),
            "right": right.lower(),
        }
        self.vk_to_name = {ord(v.upper()): k for k, v in self.key_map.items()}

        threading.Thread(target=self.clicker, daemon=True).start()
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()

    def clicker(self):
        while True:
            if "master" in toggled:
                if "left" in toggled:  # Left click
                    mouse_controller.press(Button.left)
                    time.sleep(random.uniform(0.03, 0.05))
                    mouse_controller.release(Button.left)
                    time.sleep(random.uniform(0.04, 0.08))

                if "right" in toggled:  # Right Click
                    mouse_controller.press(Button.right)
                    time.sleep(random.uniform(0.03, 0.05))
                    mouse_controller.release(Button.right)
                    time.sleep(random.uniform(0.04, 0.08))
            else:
                time.sleep(0.05)  # Avoids a busy loop

    # On press function to perform the clicks
    def on_press(self, key):
        try:
            vk = getattr(key, "vk", None)
            char = getattr(key, "char", None)

            # Reads the keys being pressed raw
            if char is not None and char.isprintable():
                vk = ord(char.upper())
            elif vk is None:
                return

            # If the virtual key matches, it toggles it
            if vk is not None and vk in self.vk_to_name:
                name = self.vk_to_name[vk]
                if name in toggled:
                    toggled.remove(name)
                    action = "removed"
                else:
                    toggled.add(name)
                    action = "added"

                # When master is toggled off, left and right are cleared
                if name == "master" and action == "added":
                    toggled.discard("left")
                    toggled.discard("right")
        except AttributeError:
            pass


if __name__ == "__main__":
    Clicker()
    try:
        while True:  # Keep background alive
            time.sleep(1)
    except KeyboardInterrupt:
        pass
