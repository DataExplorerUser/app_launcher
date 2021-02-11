import dearpygui.core as dpg
import dearpygui.simple as dpgs

# dictionary to keep track of the status of all buttons
# using it as a global variable.
# it seems that no values can be assigned to image_button
# using set_value('button1'), so the dictionary is
# used to store the status of all buttons.

# setting the starting value for all buttons to 'not selected'.

global button_status
button_status = dict({
                      'button1' : 'not selected',
                      'button2' : 'not selected'
                      })

# the button_clicked function is called by the callback of each button.
# sender is the name of the widget causing the callback. In this case,
# the sender is button1 or button2.
# the data argument can contain additional information but is usually
# empty (None) for buttons. In this case data is not used.

def button_clicked(sender, data):

    # it is needed to repeat the global statement so that
    # variables can be changed in the function.
    global button_status

    # update the status of the clicked button
    # and change the tint of the clicked button
    if button_status[sender] == 'selected':
        button_status[sender] = 'not selected'
        dpg.configure_item(sender, tint_color=None)
    else:
        button_status[sender] = 'selected'
        dpg.configure_item(sender, tint_color=[150,150,150,255])

    # update the text labels
    dpg.configure_item('status1', label='Status image 1: ' + button_status.get('button1') )
    dpg.configure_item('status2', label='Status image 2: ' + button_status.get('button2') )

# style settings for the window and font
# dpg.set_main_window_title("DearPy Gui Buttons")
dpg.add_additional_font('glacial_font.otf', 22)
dpg.set_theme_item(0, 0, 0, 0, 255) # set font colour
dpg.set_theme_item(2, 255, 255, 255, 255) # set background colour (mvGuiCol_WindowBg)

with dpgs.window('main', x_pos=0, y_pos=0, width=500, height=800):
    dpg.add_label_text('status1', label='Status image 1: not selected', parent='main')
    dpg.add_label_text('status2', label='Status image 2: not selected', parent='main', before='button1')
    dpg.add_image_button('button1', value='button1.png', height=300, width=500, frame_padding=10, callback=button_clicked)
    dpg.add_image_button('button2', value='button2.png', height=300, width=500, frame_padding=10, callback=button_clicked)
dpg.start_dearpygui(primary_window='main')