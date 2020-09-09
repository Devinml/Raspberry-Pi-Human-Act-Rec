from gpiozero import Button
import os
import lcddriver
import time
from collect_data import GetData

def init_values():
    display = lcddriver.lcd()
    white_button = Button(17)
    red_button = Button(14)
    green_button = Button(15)
    yellow_button = Button(26)
    blue_button = Button(19)
    small_button = Button(6)
    list_of_buttons = [red_button,
                       green_button,
                       white_button,
                       yellow_button,
                       blue_button,
                       small_button]
    activity_list = [i for i in range(1,7)]
    data_log = False
    return (display,
            list_of_buttons,
            data_log,
            activity_list,
            red_button,
            white_button)

def home_screen(display):
    display.lcd_display_string('White for data',1)
    display.lcd_display_string('Red for pred',2)

def get_data(display, data_log, activity_list,i,test):
    display.lcd_clear()   
    display.lcd_display_string("collecting data", 1)
    data = GetData(activity=activity_list[i], test=test)
    data.collect_data()
    display.lcd_clear()
    data_log = False
    return data_log

def enter_get_data_mode(display,test):
    test += 1 
    display.lcd_clear()
    time.sleep(1)
    data_log = True
    return (test, data_log)


def main():
    (display,
     list_of_buttons,
     data_log,
     activity_list,
     red_button,
     white_button) = init_values()
    try:
        while True:
            test = 1
            home_screen(display)
            if white_button.is_pressed:
                (test,
                data_log) = enter_get_data_mode(display,
                                                     test)
                while data_log:
                    display.lcd_display_string('Select Button',1)
                    for i in range(len(list_of_buttons)):
                        if list_of_buttons[i].is_pressed:
                            data_log = get_data(display=display,
                                                data_log=data_log,
                                                activity_list=activity_list,
                                                i=i,
                                                test=test)

            elif red_button.is_pressed:
                print('Red')
                display.lcd_display_string('red_button',1)

    except KeyboardInterrupt:
        print("Cleaning up!")
        display.lcd_clear()

if __name__ == '__main__':
    main()