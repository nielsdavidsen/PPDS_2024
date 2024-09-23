def read_word_file(filename):

    file = open(filename, "r")

    list_of_content = []

    for i, line in enumerate(file):

        if line[-1] == "\n":
            line = line[:-1]
        
        list_of_content.append((i, line))

    file.close()

    return list_of_content

def read_word_file2(filename, filter_re_str):

    file = open(filename, "r")

    list_of_content = []

    for i, line in enumerate(file):

        if line[-1] == "\n":
            line = line[:-1]
        
        list_of_content.append((i, line))

    file.close()



        
        
