import dearpygui.core as dpg
import dearpygui.simple as dpgs

# The button_clicked function is called by the callback of each button.
# Sender provides the name of the widget causing the callback. In this
# case, the sender is button1 or button2.
# The data argument can contain additional information but is usually
# empty (None) for buttons.

def button_clicked(sender, data):
    config = dpg.get_item_configuration(sender)
    dpg.log_debug(config)
    dpg.configure_item(sender, tint_color=[100, 100, 255, 255])
    dpg.configure_item('status1', label=sender+' was clicked')
    dpg.configure_item('status2', label=sender+' was clicked')


# style settings
dpg.set_main_window_size(600, 800)
dpg.set_main_window_pos(0,0)
dpg.set_main_window_title("DearPy Gui Buttons")
dpg.add_additional_font('resources/glacial_font.otf', 22)
dpg.set_theme_item(0, 0, 0, 0, 255) # set font colour
dpg.set_theme_item(2, 255, 255, 255, 255) # set background colour (mvGuiCol_WindowBg)

with dpgs.window('main', x_pos=0, y_pos=0, width=600, height=800):
    dpg.add_label_text('status1', label='Button1: not selected')
    dpg.add_label_text('status2', label='Button2: not selected')
    dpg.add_image_button('button1', value='button1.png', height=300, width=500,
                    frame_padding=20, callback=button_clicked)
    dpg.add_image_button('button2', value='button2.png', height=300, width=500,
                    frame_padding=20, callback=button_clicked)
dpg.start_dearpygui(primary_window='main')