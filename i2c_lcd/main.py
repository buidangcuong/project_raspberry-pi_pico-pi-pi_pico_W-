import i2c_lcd

def main():
    i2c_lcd.init()
    i2c_lcd.clear()
    i2c_lcd.GotoXY(0,1)
    i2c_lcd.string("hello World")
    i2c_lcd.GotoXY(1,0)
    i2c_lcd.string("respberry pi")
    
if __name__=="__main__":
    main()