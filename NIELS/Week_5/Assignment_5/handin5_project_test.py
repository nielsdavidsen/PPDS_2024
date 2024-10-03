import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import handin5_project as h5p

anomaly_data = np.genfromtxt('Land_and_Ocean_summary.txt', delimiter='', skip_header=48)
if anomaly_data.shape[0] == (2018-1850) + 1:
    print("Success: Correct number of rows")
else:
    print("Error: Incorrect number of rows")




color_mapper = h5p.ColorMapper(anomaly_data[:,1])
random_anomaly = np.random.uniform(np.min(anomaly_data[:,1]), np.max(anomaly_data[:,1]))
random_rgb = color_mapper.get_color(random_anomaly)
print("RGB for constructed random anomaly: ", random_rgb)

# Check that for anomaly value = 0 the color is white
white = color_mapper.get_color(0)
print("RGB for anomaly value = 0: ", white)



rectangles = h5p.construct_rectangles(anomaly_data[:,0], anomaly_data[:,1])

def plot_stripes(list_of_rectangles,
                 color_mapper,
                 colorbar=True,
                 figure_width=20, figure_height=5):
    """
    Visualize list of rectangles, where each rectangle is specified in the format
    (x-coordinate, y-coordinate, width, height, value). The color_mapper is
    used to look up colors corresponding to the values provided for each rectangle.

    :param list_of_rectangles: List of (x-coordinate, y-coordinate, width, height, value) tuples
    :param color_mapper: ColorMapper object used to lookup values for each block
    :param colorbar: Whether to include a color bar
    :param figure_width: Width of figure
    :param figure_height: Height of figure
    :return: None
    """

    _, ax = plt.subplots(1, figsize=(figure_width, figure_height))
    x_values = []
    y_values = []
    for rectangle in list_of_rectangles:

        anomaly_value = rectangle[-1]

        rect = matplotlib.patches.Rectangle(rectangle[:2], rectangle[2], rectangle[3],
                                            linewidth=1, edgecolor='none',
                                            facecolor=color_mapper.get_color(anomaly_value))
        ax.add_patch(rect)
        x_values += [rectangle[0], rectangle[0]+rectangle[2]]
        y_values += [rectangle[1], rectangle[1]+rectangle[3]]

    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))

    if colorbar:
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(plt.gca())
        ax_cb = divider.new_horizontal(size="1%", pad=0.1)
        matplotlib.colorbar.ColorbarBase(ax_cb, cmap=color_mapper.cmap,
                                         orientation='vertical',
                                         norm=matplotlib.colors.Normalize(
                                             vmin=color_mapper.min_value,
                                             vmax=color_mapper.max_value))
        plt.gcf().add_axes(ax_cb)
    plt.show()
    

plot_stripes(rectangles, color_mapper)




