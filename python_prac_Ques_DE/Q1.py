'''given an array of non negative numbers find first missing non-integer number in the array
for example [0,1,2,3,5] => 4    
[0,1,2,3,4] => 5
[1,2,3,4] => 0
[0,1,2,3,5,6] => 1'''



def first_missing_no(li):
    set_1= set(li) # set will be like {0,6,7,9,10}

    if 0 not in set_1:
        return 0
    elif 0 in set_1 :
        max_no_in_set, min_no_in_set= max(set_1), min(set_1)
        full_new_set= set(range(min_no_in_set, max_no_in_set+1)) # {0,1,2,3,4,5,6,7,8,9,10}
        missing_no_set = full_new_set - set_1 # {1,2,3,4,5,8}
        return (min(missing_no_set))

li= [0,6,7,9,10,6]    
print(first_missing_no(li))





            
