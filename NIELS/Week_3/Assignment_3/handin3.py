import re

def read_word_file(filename):
    with open(filename, 'r') as file:
        ''' Function that reads a file and returns tuples of the strings in the file along with their position in the file. Takes a filename as an argument.'''
        string_list = file.readlines()
        tuple_list = []
        for i, line in enumerate(string_list):
            strip_string = line.strip()
            tuple_list.append((i, strip_string))

        file.close()

        return tuple_list
    

def read_word_file2(filename, filter_re_str=''):
    with open(filename, 'r') as file:
        ''' Function that reads a file and returns tuples of the strings in the file along with their position in the file. 
        Takes a filename and a string as arguments. The string is then turned into a reg-ex (regular epxression). 
        Returns only the tuples that match the regular expression. '''

        string_list = file.readlines()
        tuple_list = []

        for i, line in enumerate(string_list):
            strip_string = line.strip()
            regex = re.compile(filter_re_str)

            if regex.search(strip_string):
                tuple_list.append((i, strip_string))

        file.close()

        return tuple_list