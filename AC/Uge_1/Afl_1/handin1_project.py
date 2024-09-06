file = open("Land_and_Ocean_summary.txt", "r")

list_of_lines = file.readlines()

file.close()


for i in range(len(list_of_lines)):

    list_of_lines[i].strip()

    if len(list_of_lines[i]) == 0 or list_of_lines[i][0] == "%":

        continue

    line = list_of_lines[i].split()

    if len(line) != 0 and int(line[0]) >= 2000:

        print(line[0])

