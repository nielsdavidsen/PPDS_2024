import sys
sys.path.append('AC/Uge_4/Afl_4')
import timeit
import handin4 as h4

wordlist_british = h4.wordfile_to_list("british-english")

wordlist_american = h4.wordfile_to_list("american-english")

start_time_linear_search = timeit.default_timer()

differences_linear_search = h4.wordfile_differences_linear_search("british-english", "american-english")

time_spent_linear_search = timeit.default_timer() - start_time_linear_search

start_time_binary_search = timeit.default_timer()

differences_binary_search = h4.wordfile_differences_binary_search("british-english", "american-english")

time_spent_binary_search = timeit.default_timer() - start_time_binary_search

