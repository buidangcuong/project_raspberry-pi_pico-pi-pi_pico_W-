from machine import Pin, PWM
import utime

def main():
    servo = PWM(Pin(15))
    servo.freq(50)
    while True:
         for angulo in range(0,181,30):
              duty =int(4.9383*angulo**2 +9000*angulo +550000)
              servo.duty_ns(duty)
              utime.sleep(1)
    
       
         for angulo in range(180,-1,-30):
             duty=int(4.9383*angulo**2+9000*angulo+550000)
             servo.duty_ns(duty)
             utime.sleep(1)
    servo.deinit()
        
   
if __name__ == '__main__':
    main()
    
