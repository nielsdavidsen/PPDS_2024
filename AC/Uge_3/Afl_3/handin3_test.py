import sys
sys.path.append('AC/Uge_3/Afl_3')

import handin3 as h3

word_list = h3.read_word_file("british-english")

filtered_word_list = h3.read_word_file2("british-english", "^py[a-z]{4}$")

print(filtered_word_list)