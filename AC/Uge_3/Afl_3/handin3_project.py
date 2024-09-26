def read_data2(filename, year_range = (0, 2025)):

    '''Reads a file and provides a list of the data lines in the files. Includes an optional filter for the year range.
    
    Parameters
    ----------
    filename : str
        The name of the file to be read.
        
    year_range : tuple
        A tuple of two integers, the first being the start year and the second being the end year.
        default: (0, 2025).
        
    Returns
    -------
    data_list : list
        A list of the data lines in the file.
    '''

    file = open(filename, "r")

    list_of_lines = file.readlines()

    file.close()

    data_list = []

    for i in range(len(list_of_lines)):

        list_of_lines0 = list_of_lines.copy()

        new_line = list_of_lines0[i].strip()

        new_line = new_line.split()

        if len(new_line) == 0 or new_line[0] == "%":

            continue

        if len(new_line) != 0 and year_range[1] > int(new_line[0]) >= year_range[0]:

            data_list.append(list_of_lines[i])

    return data_list


def read_data3(filename, year_range = (0,2025)):

    '''Reads a file and provides a list of the data lines in the files. Includes an optional filter for the year range.
    
    Parameters
    ----------
    filename : str
        The name of the file to be read.
        
    year_range : tuple
        A tuple of two integers, the first being the start year and the second being the end year.
        default: (0, 2025).
        
    Returns
    -------
    data_list : dict
        A dictionary of the data lines in the file. The key is the year and the value is a list of the data entries.
    '''

    file = open(filename, "r")

    list_of_lines = file.readlines()

    file.close()

    data_dict = {}

    for line in list_of_lines:

        line = line.strip().split()

        if len(line) == 0 or line[0] == "%":

            continue

        if len(line) != 0 and year_range[1] > int(line[0]) >= year_range[0]:

            dict_entries = line[1:]

            data_dict[int(line[0])] = [float(i) for i in dict_entries]

    return data_dict

        


    

