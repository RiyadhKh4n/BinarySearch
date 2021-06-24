import random
import time

#Implementation of binary seach algorithm
#Prove that binary seach is faster than naive seach.

'''
Naive Search: scan entre list and ask if its equal to the target
    if yes, return index[]
    if no, then return -1
'''    
#where 'l' is the list
def naive_search(l, target): 
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


#Binary Seach uses divide and conquer!
#However list must first be SORTED

def binary_search(l, target, low = None, high = None):

    if low is None:
        low = 0

    if high is None:
        high = len(l) - 1

    if high < low: #value not in list
        return -1
    
    #example l = [1, 3, 5, 10, 12, 14, 20]

    midpoint = (low + high) // 2 #2

    if l[midpoint] == target:
        return midpoint #as the midpoint == target

    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)

    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)

##########################################################################################################

if __name__ == '__main__':
    
    l = [1, 3, 4, 6, 8, 9, 11, 14, 19, 25, 30]
    target = 4
    print('The target value is in element' , naive_search(l ,target) + 1)

    #+1 is added as counting is Zero - Based
    print('The target value is in element' , binary_search(l, target) + 1)

##########################################################################################################

    length = 10000
    #build sorted list of length Ten Thousand
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3* length)) #will add random values to list from range

    sorted_list = sorted(list(sorted_list)) #saved the now sorted list into the existing variable

    start = time.time() #start time
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time() #end time
    print("Naive search time: ", (end - start) / length, " second")

    start = time.time() #start time
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time() #end time
    print("Binary search time: ", (end - start) / length, " second")