import matplotlib.pyplot as plt
import matplotlib
import numpy as np

class ColorMapper:
    """
    Wrapper class for matplotlib cmap, that maps a range of values to 
    a [0,1] range, such that values can be mapped to colors.
    """

    def __init__(self, values, cmap_str='RdBu_r'):
        """
        Constructor. Extracts min and max values from a numpy array of values, and uses 
        this to determine how to map values to colors.
    
        :param values: Numpy array of float values
        :param cmap_str: String argument for color map, which will be sent to matplotlib.
        """

        # Save attributes
        self.cmap = plt.get_cmap(cmap_str)
        self.min_value = np.min(values)
        self.max_value = np.max(values)  

        if abs(self.min_value) > abs(self.max_value):
            self.max_value = abs(self.min_value)
        else:
            self.min_value = -abs(self.max_value) 

    def get_color(self, value):
        """
        Retrieve color corresponding to a particular value.
        """
        return self.cmap((value - self.min_value) / (self.max_value - self.min_value)) 

def construct_rectangles(years, anomalies, bottom = 0.0, height = 1.0):
    width = 1
    rectangles = []
    for i in range(len(years)):
        rectangles.append((years[i], bottom, width, height, anomalies[i]))
    return rectangles