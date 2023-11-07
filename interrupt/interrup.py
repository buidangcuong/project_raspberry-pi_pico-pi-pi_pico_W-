from machine import Pin
import time

button_pin = Pin(0,Pin.IN,Pin.PULL_DOWN)
led_pin = Pin(25 , Pin.OUT)
L1 = Pin(2, Pin.OUT)
L2 = Pin(3, Pin.OUT)
L3 = Pin(4, Pin.OUT)
L4 = Pin(5, Pin.OUT)
Leds = [L1,L2,L3,L4]
count = 0

def button_callback(pin):
    global count
    count += 1
    if count == 4 :
        count =0
    print("Button pressed!")
    print("Count:", count)

button_pin.irq(trigger=Pin.IRQ_RISING, handler=button_callback)

while True:
    
    if count == 0:
        led_pin.value(0)
    elif count ==1 :
       for x in Leds:
           x.on()
           time.sleep(0.5)
           x.off()
           time.sleep(0.5)
    elif count == 2:
        for led in Leds:
            led.off()
            time.sleep(0.1)
        for i in range(3, -1, -1):
            for j in range(0,i+1):
                Leds[j].on()
                time.sleep(0.5)
                Leds[j].off()
            Leds[i].on()
    elif count == 3:
        L1.on()
        L2.on()
        time.sleep(0.1)
        L1.off()
        L2.off()
        L3.on()
        L4.on()
        time.sleep(0.1)
        L3.off()
        L4.off()
        
    time.sleep(0.1)