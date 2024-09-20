
import handin3 as h3

word_list = h3.read_word_file('british-english')


filter_re_str = '^py[a-zA-Z]{4}$'
filtered_word_list = h3.read_word_file2('british-english', filter_re_str)
print(filtered_word_list)