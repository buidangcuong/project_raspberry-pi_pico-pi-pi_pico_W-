from machine import Pin, PWM
import utime

def main():
    servo =PWM(Pin(15))
    servo.freq(50)
    while True:
          angulo =float(input('NHAP GOC QUAY:'))
          if angulo >= 0 and angulo <= 180:
             duty =int(4.9383*angulo**2 + 9000*angulo +550000)
             servo.duty_ns(duty)
        
          else:
             print('Nhap mot goc tu 0 den 180')
if __name__ =='__main__':
    main()
    