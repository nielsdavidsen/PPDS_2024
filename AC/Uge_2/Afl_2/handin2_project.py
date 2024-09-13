file = open("Land_and_Ocean_summary.txt", "r")

list_of_lines = file.readlines()

file.close()

data_list = []

for line in list_of_lines:

    line = line.strip()

    if len(line) == 0 or line[0] == "%":

        continue

    if len(line) != 0:

        data_list.append(line)

def read_data(filename = "filename"):

    file = open(filename, "r")

    list_of_lines = file.readlines()

    file.close()

    data_list = []

    for line in list_of_lines:

        new_line = line.strip()

        if len(new_line) == 0 or new_line[0] == "%":

            continue

        if len(new_line) != 0:

            data_list.append(new_line)

    return data_list

data_list_returned = read_data("Land_and_Ocean_summary.txt")

print(data_list_returned)


            