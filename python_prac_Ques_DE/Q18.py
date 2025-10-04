'''
Count Occurrences of a Word
Create a function called count_word_occurrences that takes a string and a target word as input and returns the number of times the target word appears in the string. The function should not be case-sensitive, meaning it should count occurrences regardless of the word's case. Your function should use only built-in Python tools.



>>> count_word_occurrences("The quick brown fox jumps over the lazy dog.", "the")
2  # "the" appears twice (both in lowercase and uppercase).
>>> count_word_occurrences("This is a test sentence. This sentence is a test.", "sentence")
2  # "sentence" appears twice.
>>> count_word_occurrences("Python is a versatile programming language.", "Python")
1  # "Python" appears once (case-insensitive).
>>> count_word_occurrences("No matches here.", "word")
0  # "word" does not appear in the text.

'''

def count_word_occurrences(text, word):
    # Your code here
    text_lower=text.lower().replace('.', '') 
    target_word= word.lower()
    
    
    text_list=text_lower.split() #['the','quick','brown',....]
    
    return text_list.count(target_word)
    
    
# OR

def count_word_occurrences(text, word):
    count=0
    text_lower=text.lower()
    target_word= word.lower()   
    text_list=text_lower.split() #['the','quick','brown',....]
    for item in text_list:
        if item== target_word:
            count += 1
    return count
