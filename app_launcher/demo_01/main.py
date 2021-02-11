import dearpygui.core as dpg
import dearpygui.simple as sdpg
import  time
from math import sin, cos

def style():

    # define colors (rgba)
    bg_r = 80
    bg_g = 80
    bg_b = 80
    bg_a = 255

    dpg.set_style_window_padding(0.00, 0.00)
    dpg.set_style_frame_padding(2.00, 5.00)
    dpg.set_style_item_spacing(2.00, 2.00)
    dpg.set_style_item_inner_spacing(4.00, 4.00)
    dpg.set_style_touch_extra_padding(0.00, 0.00)
    dpg.set_style_indent_spacing(20.00)
    dpg.set_style_scrollbar_size(13.00)
    dpg.set_style_grab_min_size(6.00)
    dpg.set_style_window_border_size(1.00)
    dpg.set_style_child_border_size(1.00)
    dpg.set_style_popup_border_size(1.00)
    dpg.set_style_frame_border_size(0.00)
    dpg.set_style_tab_border_size(0.00)
    dpg.set_style_window_rounding(0.00)
    dpg.set_style_child_rounding(0.00)
    dpg.set_style_frame_rounding(0.00)
    dpg.set_style_popup_rounding(0.00)
    dpg.set_style_scrollbar_rounding(0.00)
    dpg.set_style_grab_rounding(0.00)
    dpg.set_style_tab_rounding(0.00)
    dpg.set_style_window_title_align(0.00, 0.49)
    dpg.set_style_window_menu_button_position(dpg.mvDir_Left)
    dpg.set_style_color_button_position(dpg.mvDir_Right)
    dpg.set_style_button_text_align(0.50, 0.50)
    dpg.set_style_selectable_text_align(0.00, 0.00)
    dpg.set_style_display_safe_area_padding(3.00, 3.00)
    dpg.set_style_global_alpha(1.00)
    dpg.set_style_antialiased_lines(True)
    dpg.set_style_antialiased_fill(True)
    dpg.set_style_curve_tessellation_tolerance(1.25)
    dpg.set_style_circle_segment_max_error(1.60)
    dpg.set_theme_item(dpg.mvGuiCol_Text, 255, 255, 255, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TextDisabled, 102, 102, 102, 255)
    dpg.set_theme_item(dpg.mvGuiCol_WindowBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_ChildBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_PopupBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_Border, 31, 31, 31, 181)
    dpg.set_theme_item(dpg.mvGuiCol_BorderShadow, 255, 255, 255, 15)
    dpg.set_theme_item(dpg.mvGuiCol_FrameBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_FrameBgHovered, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_FrameBgActive, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_TitleBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_TitleBgActive, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_TitleBgCollapsed, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_MenuBarBg, bg_r, bg_g, bg_b, bg_a)
    dpg.set_theme_item(dpg.mvGuiCol_ScrollbarBg, 61, 61, 61, 135)
    dpg.set_theme_item(dpg.mvGuiCol_ScrollbarGrab, 105, 105, 105, 255)
    dpg.set_theme_item(dpg.mvGuiCol_ScrollbarGrabHovered, 133, 133, 133, 255)
    dpg.set_theme_item(dpg.mvGuiCol_ScrollbarGrabActive, 194, 194, 194, 255)
    dpg.set_theme_item(dpg.mvGuiCol_CheckMark, 166, 166, 166, 255)
    dpg.set_theme_item(dpg.mvGuiCol_SliderGrab, 133, 133, 133, 255)
    dpg.set_theme_item(dpg.mvGuiCol_SliderGrabActive, 163, 163, 163, 255)
    dpg.set_theme_item(dpg.mvGuiCol_Button, 138, 138, 138, 89)
    dpg.set_theme_item(dpg.mvGuiCol_ButtonHovered, 133, 133, 133, 150)
    dpg.set_theme_item(dpg.mvGuiCol_ButtonActive, 194, 194, 194, 255)
    dpg.set_theme_item(dpg.mvGuiCol_Header, 97, 97, 97, 255)
    dpg.set_theme_item(dpg.mvGuiCol_HeaderHovered, 120, 120, 120, 255)
    dpg.set_theme_item(dpg.mvGuiCol_HeaderActive, 194, 194, 194, 196)
    dpg.set_theme_item(dpg.mvGuiCol_Separator, 0, 0, 0, 35)
    dpg.set_theme_item(dpg.mvGuiCol_SeparatorHovered, 179, 171, 153, 74)
    dpg.set_theme_item(dpg.mvGuiCol_SeparatorActive, 179, 171, 153, 172)
    dpg.set_theme_item(dpg.mvGuiCol_ResizeGrip, 66, 150, 250, 64)
    dpg.set_theme_item(dpg.mvGuiCol_ResizeGripHovered, 66, 150, 250, 171)
    dpg.set_theme_item(dpg.mvGuiCol_ResizeGripActive, 66, 150, 250, 242)
    dpg.set_theme_item(dpg.mvGuiCol_Tab, 64, 64, 64, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TabHovered, 102, 102, 102, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TabActive, 84, 84, 84, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TabUnfocused, 64, 64, 64, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TabUnfocusedActive, 84, 84, 84, 255)
    dpg.set_theme_item(dpg.mvGuiCol_PlotLines, 156, 156, 156, 255)
    dpg.set_theme_item(dpg.mvGuiCol_PlotLinesHovered, 255, 110, 89, 255)
    dpg.set_theme_item(dpg.mvGuiCol_TextSelectedBg, 186, 186, 186, 89)
    dpg.set_theme_item(dpg.mvGuiCol_NavHighlight, 66, 150, 250, 255)
    dpg.set_theme_item(dpg.mvGuiCol_ModalWindowDimBg, 100, 0, 200, 255)

def update_graphs(sender, data):
    global x
    global rate
    global x_coordinates
    global sin_y_coordinates
    global cos_y_coordinates
    global frame_count
    frame_count += 1
    if frame_count >= rate:
        x = round(x, 2)
        x_coordinates.append(x)
        sin_y_coordinates.append(sin(x)*10)
        cos_y_coordinates.append(cos(x*2)*10)
        graphs = ['Graph 1', 'Graph 2', 'Graph 3', 'Graph 4']
        for graph in graphs:
            dpg.clear_plot(graph) 
            dpg.add_line_series(graph, 'sin', x_coordinates, sin_y_coordinates)
            dpg.add_line_series(graph, 'cos', x_coordinates, cos_y_coordinates)
            dpg.set_plot_xlimits(graph, xmax=x, xmin=x-10)
        frame_count = 0
        x += 0.1
    rate = dpg.get_value('Speed')

def initiate_graphs():
    global rate
    global x
    global x_coordinates
    global sin_y_coordinates
    global cos_y_coordinates
    global frame_count

    # initial values
    x = 0
    rate = 1
    frame_count = 0
    graphs = ['Graph 1', 'Graph 2', 'Graph 3', 'Graph 4']

    # UI and layout
    dpg.add_spacing(count=10)
    dpg.add_drag_float('Speed', label='Update Rate', default_value=1, 
        min_value=1, max_value=10, speed=0.01, width=600) 
    dpg.add_spacing(count=10)

    # create graphs
    with sdpg.group(name='Graph group', horizontal=True, horizontal_spacing = 5):        

        # yaxis_no_gridlines : bool = False
        # yaxis_no_tick_marks : bool = False
        # yaxis_no_tick_labels : bool = False
        # yaxis_log_scale : bool = False
        # yaxis_invert : bool = False
        # yaxis_lock_min : bool = False
        # yaxis_lock_max : bool = False

        for graph in graphs:
            dpg.add_same_line()
            dpg.add_plot(graph, height=256, width=256, anti_aliased=True, no_menus=True, no_legend=False,
            xaxis_no_tick_labels=True, yaxis_no_tick_labels=True,
            xaxis_no_tick_marks=True, yaxis_no_tick_marks=True, 
            xaxis_no_gridlines=True, yaxis_no_gridlines=True)

            x_coordinates=[0.0]
            sin_y_coordinates=[(sin(x)*10)]
            cos_y_coordinates=[(cos(x)*10)]
            dpg.add_line_series(graph, 'sin', x_coordinates, sin_y_coordinates)
            dpg.add_shade_series(graph, 'cos',  x_coordinates, cos_y_coordinates, weight=2, fill=[255, 0, 0, 100], color=[255, 0, 0, 100])
            dpg.set_plot_ylimits(graph, ymax=11, ymin=-11)

def start_graphs():
    with sdpg.window('Main Window'):
        dpg.add_text('Hello')
        dpg.enable_docking(shift_only=False, dock_space=True)
    
    with sdpg.window('Another window', x_pos=0, y_pos=600):
        dpg.add_text('Yes')

    with sdpg.window('check this window', x_pos=500, y_pos=600):
        dpg.add_text('Check this')

    with sdpg.window('Graph Window', x_pos=0, y_pos=0, autosize=True):
        dpg.set_main_window_size(1200, 600)
        dpg.set_main_window_resizable(True)

        # load font: if started by Dear PyGui showcase, then the default path is the path of the showcase
        dpg.add_additional_font('glacial_font.otf', 18)
        style()
        initiate_graphs()
    dpg.set_render_callback(update_graphs)
    dpg.start_dearpygui(primary_window='Main Window')

start_graphs()