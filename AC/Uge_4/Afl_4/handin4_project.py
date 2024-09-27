class AnomalyData:

    def __init__(self, filename, year_range = (0,2025)):

        self.filename = filename
        self.year_range = year_range

        file = open(filename, "r")

        list_of_lines = file.readlines()

        file.close()

        data_dict = {}

        for line in list_of_lines:

            line = line.strip().split()

            if len(line) == 0 or line[0] == "%":

                continue

            if len(line) != 0 and year_range[1] > int(line[0]) >= year_range[0]:

                dict_entries = line[1:]

                data_dict[int(line[0])] = [float(i) for i in dict_entries]

        self.data = data_dict

    def one_value_per_decade(self):