import re

def wordfile_to_list(filename):
    with open(filename, 'r') as file:
        ''' Function that reads a file and returns a list of words as strings'''
        string_list = file.readlines()
        return_list = []
        for line in string_list:
            strip_string = line.strip()
            return_list.append(strip_string)
        
        file.close()

    return return_list
    

def wordfile_differences_linear_search(filename1, filename2):
    ''' Function that returns a list of words that are in filename1 but not in filename2'''
    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)
    return_list = []
    for word in wordlist1:
        if word not in wordlist2:
            return_list.append(word)
    return return_list


def binary_search(sorted_list, element):
    """
    Search for element in list using binary search.
    Assumes sorted list
    """
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False


def wordfile_differences_binary_search(filename1, filename2):
    ''' Function that returns a list of words that are in filename1 but not in filename2 using binary search'''
    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)
    return_list = []
    wordlist2.sort()
    for word in wordlist1:
        if not binary_search(wordlist2, word):
            return_list.append(word)
    return return_list


def wordfile_to_dict(filename):
    ''' Function that reads a file and returns a dictionary of the words in the file as the keys'''
    with open(filename, 'r') as file:
        string_list = file.readlines()
        return_dict = {}
        for line in string_list:
            strip_string = line.strip()
            return_dict[strip_string] = None
        
        file.close()

    return return_dict


def wordfile_differences_dict_search(filename1, filename2):
    ''' 
    Function that returns a list of words that are in filename1 but not in filename2. 
    Converts filename1 to a list of words using wordfile_to_list and filename2 to a dictionary using wordfile_to_dict,
    where the keys are the words and the values are set to None 
    '''
    wordlist = wordfile_to_list(filename1)
    worddict = wordfile_to_dict(filename2)
    return_list = []
    for word in wordlist:
        if word not in worddict:
            return_list.append(word)
        
    return return_list

