from machine import Pin
import time


p0 = Pin(2, Pin.OUT)    # create output pin on GPIO0


while True:
    
    print("Led Encendido")
    p0.on()
    time.sleep(1)
    p0.off()
    print("Led Apagado")
    time.sleep(1)
