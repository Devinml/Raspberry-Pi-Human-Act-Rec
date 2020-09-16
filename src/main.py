from gpiozero import Button
import os
import lcddriver
import time
from collect_data import GetData
from featurize import DataStats, IntensityBands
import pandas as pd
import joblib

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
                scaler = joblib.load('model/scalar.pkl')
                model = joblib.load('model/log_model.pkl')
                while True:
                    running_data = GetData(activity=[0 for _ in range(6)],
                                                    test=0,
                                                    data_points=50)
                    raw = running_data.list_of_data()
                    inten_obj = IntensityBands(raw)
                    (x1, x2, x3,
                     y1, y2, y3,
                     z1, z2, z3,
                     gyro_x1, gyro_x2, gyro_x3,
                     gyro_y1, gyro_y2, gyro_y3,
                     gyro_z1, gyro_z2, gyro_z3) = inten_obj.intensity_bands()
                    stats = DataStats(raw)
                    (x_mean,
                     y_mean,
                     z_mean,
                     gyrox_mean,
                     gyroy_mean,
                     gyroz_mean,
                     x_std,
                     y_std,
                     z_std,
                     gyrox_std,
                     gyroy_std,
                     gyroz_std) = stats.get_stats()


                    data = { 'x_mean': [x_mean],
                             'y_mean':[y_mean],
                             'z_mean':[z_mean],
                             'gyrox_mean':[gyrox_mean],
                             'gyroy_mean':[gyroy_mean],
                             'gyroz_mean':[gyroz_mean],
                             'x_std':[x_std],
                             'y_std':[y_std],
                             'z_std':[z_std],
                             'gyrox_std':[gyrox_std],
                             'gyroy_std':[gyroy_std],
                             'gyroz_std':[gyroz_std],
                             'x_0_1.17':[x1],
                             'x_1.17_2.34':[x2],
                             'x_2.34_4.1':[x3],
                             'y_0_1.17':[y1],
                             'y_1.17_2.34':[y2],
                             'y_2.34_4.1':[y3],
                             'z_0_1.17':[z1],
                             'z_1.17_2.34':[z2],
                             'z_2.34_4.1':[z3],
                             'gyrox_0_1.17':[gyro_x1],
                             'gyrox_1.17_2.34':[gyro_x2],
                             'gyrox_2.34_4.1':[gyro_x3],
                             'gyroy_0_1.17':[gyro_y1],
                             'gyroy_1.17_2.34':[gyro_y2],
                             'gyroy_2.34_4.1':[gyro_y3],
                             'gyroz_0_1.17':[gyro_z1],
                             'gyroz_1.17_2.34':[gyro_z2],
                             'gyroz_2.34_4.1':[gyro_z3]}

                    X = pd.DataFrame.from_dict(data)
                    X = scaler.transform(X)
                    pred = model.predict(X)
                    if pred == 1:
                        display.lcd_clear()
                        display.lcd_display_string("Walking", 1)
                    elif pred == 2:
                        display.lcd_clear()
                        display.lcd_display_string("Walking up", 1)
                    elif pred == 3:
                        display.lcd_clear()
                        display.lcd_display_string("Walking down", 1)
                        

    except KeyboardInterrupt:
        print("Cleaning up!")
        display.lcd_clear()

if __name__ == '__main__':
    main()