from dearpygui.core import *
from dearpygui.simple import *
from math import sin, cos, tan, factorial, exp, log, sqrt, log1p, log2, log10, acos, asin, atan, atan2, acosh, asinh
from math import atanh, e, pi, fmod, expm1, pow, hypot, degrees, radians,erf, erfc, gamma, lgamma, fabs


# callbacks
def query(sender, data):
    show_item("Plot Window")
    set_plot_xlimits("Plot2", data[0], data[1])


def run_code(y, xmin, xmax, inc=100):
    y = str(y)
    code0 = "def tempfunc():\n"
    code8 = "    xmin =" + str(xmin) + "\n"
    code9 = "    xmax =" + str(xmax) + "\n"
    code1 = "    data = []\n"
    code2 = "    x = xmin\n"
    code3 = "    for i in range(0," + str(inc) + "+1):\n"
    code4 = "        y=" + y + "\n"
    code5 = "        data.append([x,y])\n"
    code6 = "        x = xmin + (1+i)*(xmax-xmin)/float(" + str(inc) + ")\n"
    code7 = "    return data"

    finalcode = code0 + code8 + code9 + code1 + code2 + code3 + code4 + code5 + code6 + code7

    try:
        exec(finalcode)
        data = eval("tempfunc()")
        return data
    except Exception as ex:
        return ex


def plot_callback(sender, data):
    clear_plot("Plot1")
    y_min = -10
    y_max = 10
    formula = "40*sin(x)"
    points = 300
    data1 = run_code(formula, y_min, y_max, points)

    x_data = []
    y_data = []
    for data in data1:
        x_data.append(data[0])
        y_data.append(data[1])

    add_line_series("Plot1", "Y1", x_data, y_data, weight=2, color=get_value("Color"))
 
with window("Main Window"):
    add_plot("Plot1", height=-1, query_callback=query)

set_resize_callback(plot_callback, handler='Main Window')
start_dearpygui(primary_window="Main Window")