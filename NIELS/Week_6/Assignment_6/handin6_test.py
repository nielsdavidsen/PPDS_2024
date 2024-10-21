
import pandas as pd
import numpy as np
import handin6 as h6

df_british = pd.read_table('british-english', keep_default_na=False, header=None)
df_british.columns = ['word']

palindromes = h6.find_palindromes(df_british, minimum_length=4)
print(palindromes)


matching_words = h6.find_words_starting_with(df_british, 'congra')
print(matching_words)
