from machine import I2C,Pin
import time

i2c =I2C(1,scl = Pin(27), sda = Pin(26), freq =270000);

def command(cmd):
    data_u =cmd&0xf0
    data_l =(cmd<<4)&0xf0
    data =[(data_u|0x0C),(data_u|0x08),(data_l|0x0c),(data_l|0x08)]
    
    for x in data:
        i2c.writeto(0x27,bytes([x]))

def data(data):
    data_u = data & 0xf0
    data_l = (data << 4) & 0xf0
    data = [(data_u | 0x0D), (data_u | 0x09), (data_l | 0x0D), (data_l | 0x09)]

    for x in data:
        i2c.writeto(0x27, bytes([x]))
        
        


def init():
    time.sleep_ms(50)
    command(0x30)
    time.sleep_ms(5)
    command(0x30)
    time.sleep_us(200)
    command(0x30)
    time.sleep_ms(10)
    command(0x20)
    time.sleep_ms(10)
    
    command(0x28)
    time.sleep_ms(10)
    command(0x08)
    time.sleep_ms(10)
    command(0x01)
    time.sleep_ms(20)
    command(0x06)
    time.sleep_ms(10)
    command(0x0c)
    time.sleep_ms(50)
    
def string(string):
    for x in string:
        val= ord(x)
        data(val)

def GotoXY(x,y):
    if(x==0):
        command(y|0x80)
        time.sleep_ms(10)
    elif(x==1):
        command(y|0xc0)
        time.sleep_ms(10)
        
def clear():
    command(0x01)
    time.sleep_ms(20)
  
    
    
    
    
    
    