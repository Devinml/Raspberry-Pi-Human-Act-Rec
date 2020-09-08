from gpiozero import Button
import os
import lcddriver
import time
from collect_data import GetData


display = lcddriver.lcd()
white_button = Button(17)
red_button = Button(14)

def home_screen():
    display.lcd_display_string('White for data',1)
    display.lcd_display_string('red for pred',2)

try:
    while True:
        test = 1
        home_screen()    
        if white_button.is_pressed:
            while True:
                if white_button.is_pressed:
                    test += 1
                    display.lcd_display_string("collecting data", 1)
                    data = GetData(activity=1, test=test)
            display.lcd_clear()
            

            
            data.collect_data()
            display.lcd_clear()
        if red_button.is_pressed:
            print('Red')
            display.lcd_display_string('red_button',1)

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()