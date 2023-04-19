import numpy as np 

# This matrix simulates protanopia, one of the most common forms of color blindness (Red-blind)
protanopia_simulation_matrix = np.array([[0.567, 0.433, 0],
                                [0.558, 0.442, 0],
                                [0, 0.242, 0.758]])

# This matrix simulates deuteranopia, another common form of color blindness (Green-blind)
deuteranopia_simulation_matrix = np.array([[0.625, 0.375, 0],
                                [0.7, 0.3, 0],
                                [0, 0.3, 0.7]])

# This matrix simulates tritanopia, a rare form of color blindness (Blue-blind)
tritanopia_simulation_matrix = np.array([[0.95, 0.05, 0],
                                [0, 0.433, 0.567],
                                [0, 0.475, 0.525]])

protanomaly_simulation_matrix = np.array([[0.817,0.183,0.000],
                                [0.333,0.667,0.000],
                                [0.000,0.125,0.875]])

deuteranomaly_simulation_matrix = np.array([[0.800,0.200,0.000],
                                [0.258,0.742,0.000],
                                [0.000,0.142,0.858]])

tritanomaly_simulation_matrix = np.array([[0.967,0.033,0.00],
                                [0.00,0.733,0.267],
                                [0.00,0.183,0.817]])

achromatopsia_simulation_matrix = np.array([[0.299,0.587,0.114],
                                [0.299,0.587,0.114],
                                [0.299,0.587,0.114]])

achromatomaly_simulation_matrix = np.array([[0.618,0.320,0.062],
                                [0.163,0.775,0.062],
                                [0.163,0.320,0.516]])

# Color ranges (in HSV format)
lower_blue = np.array([100, 50, 50]) 
upper_blue = np.array([130, 255, 255]) 

lower_green = np.array([60, 25, 0])
upper_green = np.array([180, 255, 255])

lower_red1 = np.array([0, 25, 0])
upper_red1 = np.array([30, 255, 255])
lower_red2 = np.array([150, 25, 0])
upper_red2 = np.array([180, 255, 255])

lower_yellow = np.array([30, 25, 0])
upper_yellow = np.array([60, 255, 255]) 

lower_orange1 = np.array([0, 25, 0])
upper_orange1 = np.array([30, 255, 255])
lower_orange2 = np.array([160, 25, 0])
upper_orange2 = np.array([180, 255, 255])

# BGR formatted colors
red = np.array([0, 0, 255])
blue = np.array([255, 0, 0])
green = np.array([0, 255, 0])