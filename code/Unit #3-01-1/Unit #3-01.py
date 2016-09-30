# Created by: Hamza Salman
# Course: ICS3U
# Created: September 2016
# This program is used to learn if statements

import ui

MAX_NUMBER_OF_STUDENTS = 24

def check_touch_up_inside(sender):
    # check the number of students from constant
    
    number_input = int(view['number_of_students_textfield'].text)
    if number_input > MAX_NUMBER_OF_STUDENTS:
        view['output_label'].text = 'Too many students!'

view = ui.load_view()
view.present('full_screen')
