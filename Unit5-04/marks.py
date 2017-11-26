# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program shows the user's inputted marks in a textview and calculates the user's average

import ui
marks_list = []

def enter_button_touch_up_inside(sender):
    # user inputs mark, valid marks are appended to array
    user_mark = float(view['user_mark_input_textfield'].text)
   
    if user_mark < 0 or user_mark > 100:
        view['marks_array_textview'].text = "Invalid. Please input a mark between 0 to 100."
    else:
        marks_list.append(user_mark)
        
        view['user_mark_input_textfield'].text = ""
        view['marks_array_textview'].text = "Your marks: " + str(marks_list)

def calculate_button_touch_up_inside(sender):
    # calculates average of inputted marks
    total = 0
    
    for mark_number in marks_list:
        total = total + mark_number
    
    average = total / len(marks_list)
    
    view['average_answer_label'].text = "Your average is " + "{:.2f}".format(average) + "%."
    
    return average

view = ui.load_view()
view.present('full_screen')
