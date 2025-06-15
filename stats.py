from collections import Counter
def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()
    

def get_num_words(text):
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_character_count(text):
    text = text.lower()
    c = Counter(text)
    return c