import re

def read_word_file(filename):

    '''Reads a file and provides a list of line index and line content for each line contained in the file.
    
    Parameters
    ----------
    filename : str
        The name of the file to be read.
        
    Returns
    -------
    list_of_content : list
        A list of tuples, where the first element is the line number and the second element is the line content.
    '''

    file = open(filename, "r")

    list_of_content = []

    for i, line in enumerate(file):

        if line[-1] == "\n":
            line = line[:-1]
        
        list_of_content.append((i, line))

    file.close()

    return list_of_content

def read_word_file2(filename, filter_re_str = ''):

    '''Reads a file and provides a list of line number and line content for each line, includes an optional filter.
    
    Parameters
    ----------
    filename : str
        The name of the file to be read.
    filter_re_str : str
        A regular expression string to filter the lines by.
        default: ''. No filter.
        
    Returns
    -------
    list_of_content : list
        A list of tuples, where the first element is the line number and the second element is the line content.
    '''

    file = open(filename, "r")

    list_of_content = []

    for i, line in enumerate(file):

        pattern = re.compile(filter_re_str)
        
        if line[-1] == "\n" and pattern.match(line):
            list_of_content.append((i, line[:-1]))

    file.close()

    return list_of_content



        
        
