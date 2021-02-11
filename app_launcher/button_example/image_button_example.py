import dearpygui.core as dpg
import dearpygui.simple as dpgs

with dpgs.window('main'):
    dpg.add_label_text('status1', label='Status image 1: not selected')
    dpg.add_label_text('status2', label='Status image 2: not selected')
    dpg.add_button('button1')
    dpg.set_theme_item(2, 255, 255, 255, 255) # set background colour (mvGuiCol_WindowBg)
    dpg.set_theme_item(dpg.mvGuiCol_Button, 0, 0, 100, 255)
dpg.start_dearpygui(primary_window='main')