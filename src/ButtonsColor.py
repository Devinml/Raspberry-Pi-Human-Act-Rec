from gpiozero import Button, LED
from time import sleep

class ButtonsColor(Button):

    def __init__(self,pin,color):
        Button.__init__(self,pin)
        self.color = color


if __name__ == '__main__':
    red_button = ButtonsColor(18, 'red')
    green_button = ButtonsColor(15, 'green')
    white_button = ButtonsColor(17, 'white')
    
    button_list = [red_button,
                   green_button,
                   white_button]
    
    while True:
        sleep(.02)
        for button in button_list:
            if button.is_pressed:
                print(f'{button.color} true')
        
