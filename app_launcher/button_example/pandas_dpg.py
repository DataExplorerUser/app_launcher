from dearpygui.core import *
from dearpygui.simple import *
import pandas as pd

def plot_callback():
    # create dataframe
    df = pd.DataFrame( {'time': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0],
                        'data': [1.0, 2.0, 6.0, 15.0, 4.0, 10.0, 6.0, 20.0, 4.0, 5.0, 3.0, 1.0, 2.0, 10.0, 20.0, 1.0, 6.0] }  )

    # getting data fromdata frame
    time = df['time']
    data = df['data']

    print(type(time))
    print(type(data))

    # converting to floats because we stored using ints (if the data is already floats this is not necessary)
    data_x = []
    data_y = []

    for i in range(len(data)):
        data_x.append(float(time[i]))
        data_y.append(float(data[i]))

    print(type(data_x))
    print(type(data_y))

    # plot dataframe
    clear_plot("Plot")
    add_line_series("Plot", "Data", data_x, data_y)
    add_scatter_series("Plot", "Data", data_x, data_y)

with window("Main Window"):
    add_text("Tips")
    add_text("This example requires the pandas python module", bullet=True)
    add_text("This example reads and writes to a cvs file with the pandas dataframe object", bullet=True)
    add_text("It also plots the data from the dataframe", bullet=True)
    add_text("Plots in DPG require the data is a float list", bullet=True)
    add_plot("Plot", height=-1)
    set_color_map("Plot", 1)
    plot_callback()
start_dearpygui(primary_window="Main Window")