from gpiozero import LEDBoard

tree = LEDBoard(*range(2,28),pwm=True)
tree.off()

