
class AnomalyData:
    def __init__(self, filename, year_range=False):
        '''Constructor that takes two arguments as input: a filename and a year range. 
        It assigns an attribute to the class called data which is a dictionary of the lines 
        in the file within the specified year range, excluding empty lines and comments. 
        The keys of the dictionary are the years of each line in the file. 
        The values are lists of the data in each line where each entry in the list
        is converted to float. 
        If no year range is specified, the function returns all lines in the file.'''

        # Opening file in read mode
        with open(filename, "r") as file:
            # Reading the file and storing the lines in a list
            list_of_lines = file.readlines()

        new_dict = {}
        for l in list_of_lines:
            # Removing the newline character from the end of the line and white spaces
            l = l.strip()

            # Checking if the line is empty or a comment
            if len(l) == 0 or l[0] == '%':   
                continue

            l_split = l.split()
            l_year = int(l_split[0])


            if not year_range:
                dict_value = l_split[1:]
                dict_value = [float(i) for i in dict_value]
                new_dict[l_year] = dict_value

            elif year_range[0] <= l_year and  year_range[1] > l_year:
                dict_value = l_split[1:]
                dict_value = [float(i) for i in dict_value]
                new_dict[l_year] = dict_value

            file.close()
        
        self.data = new_dict

    
    def one_value_per_decade(self):
        '''Method that returns a dictionary of the average anomaly value for each decade in the data.'''
        new_dict = {}
        for key in self.data:
            decade = key % 10
            if decade == 0:
                new_dict[key] = self.data[key]
                
        return new_dict
    

            




