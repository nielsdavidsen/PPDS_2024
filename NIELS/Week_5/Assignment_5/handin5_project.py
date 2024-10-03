import numpy as np
import matplotlib.pyplot as plt


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

        # Ensure that the color map is symmetric around 0
        if abs(self.min_value) > abs(self.max_value):
            self.max_value = abs(self.min_value)
        else:
            self.min_value = -abs(self.max_value)        

    def get_color(self, value):
        """
        Retrieve color corresponding to a particular value.
        """
        return self.cmap((value - self.min_value) / (self.max_value - self.min_value))    
    

def construct_rectangles(years, anomalies, bottom=0.0, height=1.0):
    """
    Construct a list of rectangles, where each rectangle is a tuple of the format
    (year, bottom coordinate of rectangle, width (set to 1), height of rectangle, anomaly_value).

    :param years: List of years
    :param anomalies: List of anomaly values
    :param bottom: Bottom coordinate of all rectangles (default 0.0)
    :param height: Height of all rectangles (default 1.0)


    :return: List of tuples
    """
    
    tuple_list = []
    for i in range(len(years)):
        tuple_list.append((years[i], bottom, 1, height, anomalies[i]))
    
    return tuple_list