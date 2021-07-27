from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10) # Extension Board - SP/MOSI

while True:
    led1.on()
    sleep(0.1)
    led1.off()
    sleep(0.1)
    
    led2.on()
    sleep(0.1)
    led2.off()
    sleep(0.1)
    
    led3.on()
    sleep(0.1)
    led3.off()
    sleep(0.1)
    
    led4.on()
    sleep(0.1)
    led4.off()
    sleep(0.1)