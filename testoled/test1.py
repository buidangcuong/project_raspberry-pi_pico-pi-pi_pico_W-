from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Thiết lập giao tiếp I2C
i2c = I2C(0, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Viết chữ "Xin chào" lên màn hình
oled.text("Xin chao", 0, 0)
oled.show()