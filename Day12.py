'''
First non-repeating character in the given string from the given input by the user 
custom input if str is = "total", answer will be 'o', similarly the second non-repeating char is also taken.
complexity is O(n)
'''
def nonrepeat(string):
    #create an empty dictonary 
    freq = {}
    
    for x in string:
        #initialise the given dict with char as repeating
        freq[x] = freq.get(x,0)+1
    
    for i in string:
        #if frequency of the char is one then return the char with one time repeated.
        if freq[i]==1:
            return i
            
    return -1
    
print(nonrepeat("total"))
# 'o'

'''
Removing the specified char form the given string by user

'''
def delete_char(string,c):
    s=""
    for x in string:
        #check for given char
        if x != c:
            s+=x      
    print(s)
    
delete_char("pb999b",'b')
# result p999

'''
Reverse the string
'''
#using slicing
s = "total"

print(s[::-1])

#iterative way
s= "total"
r=""
#come back from the last index
for x in range(len(s)-1,-1,-1):
    r+=s[x]
print(r) 

# output - "latot"   
    


