def wordfile_to_list(filename):

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    list_of_lines = [line.strip() for line in lines]

    return list_of_lines

def wordfile_differences_linear_search(filename1, filename2):

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

    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)

    wordlist2.sort()

    differences = []

    for word in wordlist1:
        if not binary_search(wordlist2, word):
            differences.append(word)

    return differences