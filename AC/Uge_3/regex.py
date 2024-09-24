import re

pattern = re.compile(r"(\d{2})-(\d{2})-(\d{4})") # 2 digits, 2 digits, 4 digits for example. The specifications come in the ""

match = pattern.match("12-12-2012") # This is a match, because the string is in the correct format. Now we can extract the groups.

print(match.groups()) # ('12', '12', '2012') - the groups are the parts of the string that match the specifications in the pattern.

data = '''# Measurements started
Sep 9, 9:05, T=22deg
SEP 9, 10:15, T=25deg
# Taking a coffee break
Sep 9, 11:15, T=-10deg
# Weekend
Sept 12, 09:00AM, T=32deg
Oct12 13:00, T=32degr'''


data_lines = data.split('\n')

mypattern = re.compile(r"^([a-zA-Z]+ ?[0-9]+),? ?([0-9]*:[0-9]+[A-Z]*), ([A-Za-z]*=-*[0-9]*[a-s]*)")

for data_line in data_lines:

    match = mypattern.match(data_line)

    if match:
        print(data_line)

    