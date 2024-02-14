#check the given array is balanced or not
lis = ['{','}','{','}','}']
stack = []

for i in lis:
    if i == '{':
        stack.append(i)
    else:
        if len(stack) == 0 or stack.pop() != '{':
            print(0)
            break
else:
    if len(stack) == 0:
        print(1)
    else:
        print(0)
        
'''
We use a stack to keep track of opening braces {.
When we encounter a closing brace }, we check if the stack is empty (which means we have an unbalanced number of closing braces) or if the top of the stack contains a matching opening brace. If not, the braces are unbalanced.
At the end, we check if the stack is empty (all opening braces are matched), and print the result accordingly.
'''
#Output: 0
