from gpiozero import LED, Button, Buzzer
from time import sleep

button = Button(2)
buzzer = Buzzer(15)
redLED = LED(17)
yellowLED = LED(27)
greenLED = LED(22)

while True:
    if button.is_pressed:
        buzzer.on()
        greenLED.off()
        
        yellowLED.on()
        sleep(2)
        yellowLED.off()
        
        redLED.on()
        sleep(5)
        redLED.off()
        
        greenLED.on()
        sleep(5)
    else:
        greenLED.on()
        buzzer.off()