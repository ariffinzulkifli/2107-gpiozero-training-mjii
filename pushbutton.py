from gpiozero import Button, LED
from time import sleep

button = Button(2)
led = LED(17)

while True:
    if button.is_pressed:
        print("Pushbutton Pressed")
        led.on()
    else:
        print("Pushbutton Released")
        led.off()
    sleep(1)