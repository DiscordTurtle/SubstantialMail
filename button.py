from gpiozero import Button, LED

button_high = LED(26)
button_high.off()
button = Button(19)

def set_callback(callback):
    button.when_pressed = callback