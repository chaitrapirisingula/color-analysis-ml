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