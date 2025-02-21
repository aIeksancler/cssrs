from pynput.mouse import Listener, Controller
import random
import time

# Initialize the mouse controller
mouse = Controller()

# Click tracking variables
click_times = []
freeze_mode = False

def dice_roll(number):
    return random.randint(0, number) == 0

def on_click(x, y, button, pressed):
    global freeze_mode
    if not pressed:
        return
    
    current_time = time.time()
    click_times.append(current_time)
    
    # Remove old clicks (keep only last 3 seconds of history)
    click_times[:] = [t for t in click_times if current_time - t < 1]
    
    if len(click_times) > 3:
        freeze_mode = True
        print("freeze")
    elif len(click_times) <= 2:
        freeze_mode = False
        print("unfreeze")
    
    if not freeze_mode and dice_roll(5):
        dx, dy = random.randint(-8, 2), random.randint(-2, 8)
        mouse.move(dx, dy)
        
# Start listening to mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
