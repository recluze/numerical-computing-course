### Matplotlib style. No need to modify
import matplotlib.pyplot as plt
import numpy as np 
np.random.seed(1337)


plt.style.use("dark_background")

plt.rcParams.update({
    "font.family": 'Fira Sans', 
    "font.size": 16,
    "axes.labelpad": 30, 
    "axes.titlepad": 30,
    "axes.facecolor": "#2E3440",
    "grid.color": "#4c566a", 
    "grid.linestyle": "--",
    "figure.facecolor": "#2E3440",
    "savefig.facecolor": "#333333",
    "savefig.dpi": 600,
    "figure.autolayout" : True,
})


# Nord colors: 
nord_red     = "#bf616a"
nord_orange  = "#d08770"
nord_yellow  = "#ebcb8b"
nord_green   = "#a3be8c" 
nord_blue    = "#5e81ac" 
nord_violet  = "#b48ead" 

nord_gray_b  = "#2e3440"
nord_gray_g0 = "#3b4252" 
nord_gray_g0 = "#434c5e" 
nord_gray_g0 = "#4c566a" 
nord_gray_g0 = "#d8dee9" 
nord_gray_g0 = "#e5e9f0" 
nord_gray_w  = "#eceff4" 


# Markers: x, ^, v, ., o, 
# Circle marker: plot: mfc='none' , scatter: facecolor='none'



def put_marker(plt, x, y, style='wo', markersize=30, **kwargs): 
    plt.plot(x, y, style, markersize=markersize, **kwargs)
    
    
def put_guide(plt, x_mark, y_mark, x_min, y_min, color=nord_yellow, linestyle='--', linewidth=1):
    plt.plot([x_mark, x_mark, x_min], [y_min, y_mark, y_mark], color=color , linestyle=linestyle, linewidth=linewidth)
