from gpiozero import Buzzer, LED
from time import sleep

buzzer = Buzzer(15)
led = LED(17)

while True:
    buzzer.on()
    led.on()
    sleep(0.3)
    buzzer.off()
    led.off()
    sleep(0.3)