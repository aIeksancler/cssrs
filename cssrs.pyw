from pynput.mouse import Listener, Controller
import random

# Initialize the mouse controller
mouse = Controller()

def dice_roll(number):
    return random.randint(0, number) == 0

def on_click(x, y, button, pressed):
    if pressed and dice_roll(5):
        mouse.move(random.randint(-5, 5), random.randint(-5, 5))  # Adjust the values as needed

# Start listening to mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
