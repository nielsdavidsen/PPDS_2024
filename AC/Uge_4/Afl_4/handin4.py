def wordfile_to_list(filename):

    '''Converts a file with words to a list of words.
    
    Parameters:
    ----------
    filename : str
        The name of the file to be read.
        
    Returns:
    -------
    list_of_lines : list
        A list of the words in the file.
    '''

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    list_of_lines = [line.strip() for line in lines]

    return list_of_lines

def wordfile_differences_linear_search(filename1, filename2):

    '''Finds the difference between two files with words using linear search. 
    Figures out which words are in the first file but not in the second.
    
    Parameters:
    ----------
    filename1 : str
        The name of the first file to be read.
    filename2 : str
        The name of the second file to be read.
        
    Returns:
    -------
    differences : list
        A list of the words in the first file that are not in the second.
    '''

    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)

    differences = []

    for word in wordlist1:
        if word not in wordlist2:
            differences.append(word)

    return differences

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

    '''Finds the difference between two files containing words, using binary search. 
    Figures out which words are in the first file but not in the second.

    Parameters:
    ----------
    filename1 : str
        The name of the first file to be read.
    filename2 : str 
        The name of the second file to be read.

    Returns:
    -------
    differences : list
        A list of the words in the first file that are not in the second.
    '''

    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)

    wordlist2.sort()

    differences = []

    for word in wordlist1:
        if not binary_search(wordlist2, word):
            differences.append(word)

    return differences

def wordfile_to_dict(filename):

    '''Converts a file with words to a dictionary of words.
    
    Parameters:
    ----------
    filename : str
        The name of the file to be read.
        
    Returns:
    -------
    dict_of_lines : dict
        A dictionary of the words in the file.
    '''

    file = open(filename, 'r')

    lines = file.readlines()

    file.close()

    dict_of_lines = {line.strip(): None for line in lines}

    return dict_of_lines

def wordfile_differences_dict_search(filename1, filename2):

    '''Finds the difference between two files containing words. 
    Makes one a list, and the other a dictionary, and then looks up the entries from the list in the dictionary.
    
    Parameters:
    ----------
    filename1 : str
        The name of the first file to be read.
    filename2 : str
        The name of the second file to be read.
        
    Returns:
    -------
    differences : list
        A list of the words in the first file that are not in the second.
    '''

    wordfile1 = wordfile_to_list(filename1)
    wordfile2 = wordfile_to_dict(filename2)

    differences = []

    for word in wordfile1:
        if word not in wordfile2:
            differences.append(word)    

    return differences



