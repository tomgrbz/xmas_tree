from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)
leds = [4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23, 22]

for k, v in enumerate(leds):
    if k == len(leds) - 1:
        tree.off()
    tree[k].source_delay = 0.5
    tree[k].source = random_values()
    
pause()

