from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
leds = [[22, 19, 4], [8, 23, 17], [16, 24, 2, 13, 15], [12, 14, 20, 7, 3, 6], [9, 18, 11, 5, 21, 10]]
tree_copy = [4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23, 22]
tree = LEDBoard(4, 15, 13, 21, 25, 8, 5, 10, 16, 17, 27, 26, 24, 9, 12, 6, 20, 19, 14, 18, 11, 7, 23, 22, pwm=True)


num_turned_on = 0
for k, v in enumerate(leds):
    map(lambda x: tree[tree_copy.index(x)].off(), leds[k])
    for i, j in enumerate(leds[k]):
        tree[tree_copy.index(j)].on()
    # #num_turned_on += 1
    # # tree[k].source_delay = 0.5
    # # tree[k].source = random_values()
    # #tree[k].on()
        print(leds[k][i])
    # # tree[k].off()
        tree[tree_copy.index(j)].off()


    
    
pause()



# def turn_off_all():
#     tree.off()
# while True:
#     for led in tree[:9]:
#         led.source = random_values()
#         sleep(0.2)
        
#     turn_off_all()
#     sleep(1)
#     for led in tree[10:20]:
#         led.source = random_values()
#         sleep(0.2)
#     turn_off_all()

