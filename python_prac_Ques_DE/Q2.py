'HOw will you count the occurrence of a specific word in a string/list ?'
# case 1: if string 
sentence = "apple banana apple orange apple banana"
word = "apple"
conv_list= sentence. split().count(word)
print (conv_list)

#ANOTER METHOD
from collections import Counter
conv_list = sentence.split()
word_count= Counter(conv_list)
print(word_count)

#ANOTHER METHOD WITHOUT USNG FUNCTION
word_in_dict ={}
sentence_list= sentence. split() #['apple','banana','apple','orange','apple','banana' ]

for item in sentence_list:
    if item in word_in_dict:
        word_in_dict[item] += 1  # word_in_dict[item] is a key in dict and +=1 will increase the count by 1 
    else:
        word_in_dict[item] =1 # if key not present in dict then it will add the key and assign value 1

print(word_in_dict) # {'apple': 3, 'banana': 2, 'orange': 1}





'''
given 2 strings return true if one is anagram of another 
'''

'''
given a string containing paranthesis character '(' , ')' , '{' , '}' , '[' , ']'
uou have to determine if the input string is valid or not '''


'''
Given an array of distinct integers, determine the minimum absolute difference between any two elements. 
Print all element pairs with that difference in ascending order.
Example:
numbers = [6, 2, 4, 10]
The minimum absolute difference is 2, and the pairs with that difference are (2, 4) and (4, 6).
Output:
2 4
4 6
'''


'''


'''