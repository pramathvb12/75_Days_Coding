'''
Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, 
printing the value of each non-zero valued index that number of times.
Given a list of integers, count and return the number of times each value appears as an array of integers.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    #list of 100 items and initialise to 0
    lst = [0]*100
    #check if element in array
    for i in arr:
        #increment the position of num
        lst[i] += 1
    return lst
                      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either pangram or not pangram as appropriate.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    #get every alpahbet from english 
    alphabet = list(string.ascii_lowercase)
    
    s = s.lower()
    #compare the difference between two sets 
    if len(set(alphabet).difference(set(s))) > 0:
        return "not pangram"
    else:
        return "pangram"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

