import numpy as np

def read_mnist_csv(filename):
    '''Turns a datafile into a numpy array.
    
    Parameters
    ----------
    filename : str
        The name of the file to be read.
        
    Returns
    -------
    np.array
        The data from the file as a numpy array.
    ''' 
    return np.genfromtxt(filename, delimiter=',', skip_header=1)

def group_by_label(array):

    grouped_list_of_arrays = []
    label = array[:,0]

    max_val = int(np.max(label))

    for i in range(max_val + 1):

        val = np.where(label == i)

        grouped_list_of_arrays.append(array[val])

    return grouped_list_of_arrays

def get_image(digit_image_groups, digit):
    return digit_image_groups[digit][np.random.randint(0,10), 1:].reshape(28,28) 


        
