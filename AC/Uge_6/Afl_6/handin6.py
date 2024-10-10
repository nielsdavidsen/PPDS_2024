import pandas as pd

def find_palindromes(word_dataframe, minimum_length = 4):
    '''Find palindromes of a minimal desired length in a pandas DataFrame of words. 
    Excludes words containing apostrophes. Is case insensitive.
    
    Parameters
    ----------
    word_dataframe : pandas.DataFrame
        DataFrame containing words in a column named 'words'.
    minimum_length : int, optional
        Minimum length of a palindrome. Default is 4.
        
    Returns
    -------
    palindromes : pandas.DataFrame
        DataFrame containing the palindromes found in the 'words' column.
    '''

    apostrophe_mask = word_dataframe['words'].str.contains("'", na=False)
    length_mask = word_dataframe['words'].str.len() >= minimum_length

    df_palindromes = word_dataframe[~apostrophe_mask & length_mask]

    return df_palindromes

def find_words_starting_with(word_dataframe, prefix):
    '''Find words starting with a given prefix in a pandas DataFrame of words.
    Excludes words containing apostrophes. Is case insensitive.

    Parameters
    ----------
    word_dataframe : pandas.DataFrame
        DataFrame containing words in a column named 'words'.
    prefix : str
        Prefix to search for.

    Returns
    -------
    found_words : pandas.DataFrame
        DataFrame containing the wordsin the 'words' column matching the criteria.
    '''
    apostrophe_mask = word_dataframe['words'].str.contains("'", na=False)
    prefix_mask = word_dataframe['words'].str.startswith(prefix, na=False)

    found_words = word_dataframe[~apostrophe_mask & prefix_mask]  

    matching_dict = {}

    for word in found_words['words']:
        matching_dict[str(len(word))] = [words for words in found_words['words'] if len(words) == len(word)]

    return matching_dict
