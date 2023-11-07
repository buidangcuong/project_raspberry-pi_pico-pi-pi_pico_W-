from machine import Pin
import time

L1 = Pin(2, Pin.OUT)
L2 = Pin(3, Pin.OUT)
L3 = Pin(4, Pin.OUT)
L4 = Pin(5, Pin.OUT)

L5 = Pin(6, Pin.OUT)
L6 = Pin(7, Pin.OUT)
L7 = Pin(8, Pin.OUT)
L8 = Pin(9, Pin.OUT)
count = 0
nut1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
leds = [L1, L2, L3, L4, L5, L6, L7, L8]
delay = 0.25

def switch_case(count):
    if count == 1:
        for x in leds:
            x.on()
            time.sleep(delay)
            x.off()
            time.sleep(delay)
    elif count == 2:
        for i in range(len(leds)):
            leds[i].on()
            time.sleep(delay)
            leds[i].off()

            if i < len(leds) - 1:
                leds[len(leds) - 1 - i].on()
                time.sleep(delay)
                leds[len(leds) - 1 - i].off()
    elif count == 3:
        count = 0
    else:
      return

while True:
   
    if nut1.value():
        time.sleep(0.01)
        if nut1.value():
            count+=1
            print(count)
            if count == 3 and nut1.value():
                count =0
        while nut1.value():
            time.sleep(0.01)
        switch_case(count)    
              
                
         

 
