import numpy as np

def read_mnist_csv(filename):
    ''' Function that reads a csv file and returns a numpy array of the data in the file. Takes a filename as an argument.'''
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    return data


def group_by_label(np_array):
    ''' Function that takes a numpy array as an argument and groups the data by the value of the 
        first entry in every row (values being digits between 0-9). 
        Returns a list of numpy arrays where each element is a group of data with the same digit as the first value in the row. '''
    
    labels = np_array[:, 0]
    N_digits = int(np.max(labels))

    grouped_data = []
    for i in range(N_digits + 1):
        grouped_data.append(np_array[labels == i])
    
    return grouped_data


def get_image(digital_image_groups, digit):
    ''' Function that takes a list of numpy arrays and an integer as arguments. 
        The function returns a random image in the group of images that has the same digit as the integer argument. '''
    for index in range(len(digital_image_groups)):
        if digital_image_groups[index][0, 0] == digit:
            rand_index = np.random.randint(0, len(digital_image_groups[index]))

            # the [rand_index, 1:] get a random entry in the desired array and then remove the first element in the row which is the digit
            return digital_image_groups[index][rand_index, 1:].reshape(28, 28)


    