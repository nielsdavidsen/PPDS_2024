# Opening file in read mode
file = open("Land_and_Ocean_summary.txt", "r")

# Reading the file and storing the lines in a list
list_of_lines = file.readlines()

# Closing the file
file.close()

data_list = []

for n in list_of_lines:
    # Removing the newline character from the end of the line and white spaces
    n = n.strip('\n')
    n = n.strip()   

    # Checking if the line is empty or a comment
    if len(n) == 0 or n[0] == '%':   
        continue
    
    else:            
        data_list.append(n)



def read_data(filename):
    '''Function takes a filename as input and returns a list of the lines in the file, excluding empty lines and comments. It returns a list of strings where each string is  a line in the data file.'''
    # Opening file in read mode
    file = open(filename, "r")

    # Reading the file and storing the lines in a list
    list_of_lines = file.readlines()

    # Closing the file
    file.close()

    data_list = []

    for l in list_of_lines:
        # Removing the newline character from the end of the line and white spaces
        l = l.strip('\n')
        l = l.strip()   

        # Checking if the line is empty or a comment
        if len(l) == 0 or l[0] == '%':   
            continue
        
        else:              
            data_list.append(l)

    return data_list

data_list_returned = read_data("Land_and_Ocean_summary.txt")
print(data_list_returned)


