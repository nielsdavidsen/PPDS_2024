
import handin4 as h4
import timeit



wordlist_british = h4.wordfile_to_list('british-english')


start_time_linear_search = timeit.default_timer()
differences_linear_search = h4.wordfile_differences_linear_search('british-english', 'american-english')
time_spent_linear_search = timeit.default_timer() - start_time_linear_search
print('Time spent on linear search: ', time_spent_linear_search)


start_time_binary_search = timeit.default_timer()
differences_binary_search = h4.wordfile_differences_binary_search('british-english', 'american-english')
time_spent_binary_search = timeit.default_timer() - start_time_binary_search
print('Time spent on binary search: ', time_spent_binary_search)


worddict_american = h4.wordfile_to_dict('american-english')

start_time_dict_search = timeit.default_timer()
differences_dict_search = h4.wordfile_differences_dict_search('british-english-test', 'american-english-test')
time_spent_dict_search = timeit.default_timer() - start_time_dict_search
print('Time spent on dict search: ', time_spent_dict_search)

