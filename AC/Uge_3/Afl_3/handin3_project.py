def read_data2(filename, year_range = (0, 2024)):

    file = open(filename, "r")

    list_of_lines = file.readlines()

    file.close()

    data_list = []

    for i in range(len(list_of_lines)):

        list_of_lines0 = list_of_lines.copy()

        new_line = list_of_lines0[i].strip()

        new_line = new_line.split()

        if len(new_line) == 0 or new_line[0] == "%":

            continue

        if len(new_line) != 0 and year_range[1] > int(new_line[0]) >= year_range[0]:

            data_list.append(list_of_lines[i])

    return data_list