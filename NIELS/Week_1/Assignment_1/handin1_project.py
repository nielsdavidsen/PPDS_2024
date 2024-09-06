# Opening file in read mode
file = open("Land_and_Ocean_summary.txt", "r")

# Reading the file and storing the lines in a list
list_of_lines = file.readlines()

# Closing the file
file.close()


for l in list_of_lines:
    # Removing the newline character from the end of the line and white spaces
    l = l.strip('\n')
    l = l.strip()   

    # Checking if the line is empty or a comment
    if len(l) == 0 or l[0] == '%':   
        continue

    else:            
        # Splitting the line into words
        words = l.split()

        # Print the year (first word)
        if int(words[0]) >= 2000:
            print(words[0])
            
