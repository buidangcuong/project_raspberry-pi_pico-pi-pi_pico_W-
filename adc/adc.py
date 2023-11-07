from machine import ADC
import time


adc = ADC(4)
while True:
    voltage = adc.read_u16()*3.3/65535
    
    temp = 27-(voltage-0.706)/0.001721
    print(temp)
    time.sleep(1)
 