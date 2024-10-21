
def find_palindromes(word_dataframe, minimum_length=4):
    '''
    A function that takes a pandas DataFrame with a column 'word' and returns a new DataFrame 
    with only the words that are palindromes and have a minimum length of characters specified when 
    calling the function. The minimum length is 4 by default. The function is case insensitive, but leaves
    out words with appostrophes.

    Parameters:
    ----------------
    word_dataframe (pandas DataFrame): 
        A DataFrame with a column 'word' containing words (strings).

    minimum_length (int): 
        The minimum length of the words to be included in the output DataFrame.

    
    Returns:
    ----------------
    pandas DataFrame: 
        A DataFrame with only the words that are palindromes and have a minimum length of characters specified
    '''

    # Make all words lowercase
    word_dataframe['word'] = word_dataframe['word'].str.lower()

    # Find all palindromes
    mask_palindrome = word_dataframe['word'] == word_dataframe['word'].str[::-1]

    # Find all words with a minimum length
    mask_minlength = word_dataframe['word'].str.len() >= minimum_length

    # No appostrophes
    mask_noappostrophes = ~word_dataframe['word'].str.contains("'")
    

    mask_combined = mask_palindrome & mask_minlength & mask_noappostrophes

    return word_dataframe[mask_combined]



def find_words_starting_with(word_dataframe, prefix):
    '''
    A function that takes a prefix string and a DataFrame with a column 'word' and returns a dictionary with the words staring with the prefix. 
    The keys of the dictionary are the length of the words and the values are lists of words with that length. The function is case insensitive, but leaves
    out words with appostrophes.

    Parameters:
    ----------------

    word_dataframe : pandas DataFrame
        A DataFrame with a column 'word' containing words (strings).

    prefix : str
        A string with the prefix to search for in the words.

    Returns:
    ----------------
    dict: 
        A dictionary with the words starting with the prefix. The keys are the length of the words and the values are lists of words with that length.


    '''

    return_df = word_dataframe.copy()

    word_dataframe['word'] = word_dataframe['word'].str.lower()

    # Find all words starting with the prefix
    mask_startswith = word_dataframe['word'].str.startswith(prefix)

    # No appostrophes
    mask_noappostrophes = ~word_dataframe['word'].str.contains("'")

    mask_combined = mask_startswith & mask_noappostrophes

    return_df = return_df[mask_combined]

    return_dict = {}
    # Group by length of words
    grouped_obj = return_df.groupby(return_df['word'].str.len())

    for key, item in grouped_obj:
        return_dict[key] = item['word'].tolist()

    return return_dict




    




