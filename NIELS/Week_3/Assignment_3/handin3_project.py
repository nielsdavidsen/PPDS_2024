
def read_data2(filename, year_range=(0,0)):
    '''Function takes two arguments as input: a filename and a year range. It returns a list of the lines in the file within the specified year range, excluding empty lines and comments. 
    Each line in the file is converted to a string. If no year range is specified, the function returns all lines in the file.'''

    # Opening file in read mode
    with open(filename, "r") as file:
        # Reading the file and storing the lines in a list
        list_of_lines = file.readlines()

    data_list = []
    for l in list_of_lines:
        # Removing the newline character from the end of the line and white spaces
        l = l.strip()

        # Checking if the line is empty or a comment
        if len(l) == 0 or l[0] == '%':   
            continue

        l_split = l.split()
        l_year = int(l_split[0])

        if year_range[0] == 0 and year_range[1] == 0:
            cleaned_line = ', '.join(l_split)
            data_list.append(cleaned_line)

        elif year_range[0] <= l_year and  year_range[1] > l_year:
            cleaned_line = ', '.join(l_split)
            data_list.append(cleaned_line)               

        file.close()
    return data_list



def read_data3(filename, year_range=False):
    '''Function takes two arguments as input: a filename and a year range. It returns a dictionary of the lines in the file within the specified year range, excluding empty lines and comments. 
    The keys of the dictionary are the years of each line in the file. The values are lists of the data in each line where each entry in the list is converted to float. 
    If no year range is specified, the function returns all lines in the file.'''

    # Opening file in read mode
    with open(filename, "r") as file:
        # Reading the file and storing the lines in a list
        list_of_lines = file.readlines()

    new_dict = {}
    for l in list_of_lines:
        # Removing the newline character from the end of the line and white spaces
        l = l.strip()

        # Checking if the line is empty or a comment
        if len(l) == 0 or l[0] == '%':   
            continue

        l_split = l.split()
        l_year = int(l_split[0])

        
        if not year_range:
            dict_value = l_split[1:]
            dict_value = [float(i) for i in dict_value]
            new_dict[l_year] = dict_value

        elif year_range[0] <= l_year and  year_range[1] > l_year:
            dict_value = l_split[1:]
            dict_value = [float(i) for i in dict_value]
            new_dict[l_year] = dict_value
        
        file.close()
    return new_dict