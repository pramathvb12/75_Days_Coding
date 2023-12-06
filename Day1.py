# HackerRank List Solution

# Question

'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of 
commands where each command will be of the  types listed above. Iterate 
through each command in order and perform the corresponding operation 
on your list.
'''

# Solution

def main():
    N = int(input())
    
    my_list = []
    
    for i in range(N):
        op = input().split()
        
        if op[0] == 'insert':
            my_list.insert(int(op[1]),int(op[2]))
        elif op[0] == 'remove':
            my_list.remove(int(op[1]))
        elif op[0] == 'sort':
            my_list.sort()
        elif op[0] == 'append':
            my_list.append(op[1])
        elif op[0] == "reverse":
            my_list.reverse()
        elif op[0] == "pop":
            my_list.pop()
        elif op[0] == "print":
            print(my_list)
        else:
            print("Some wrong operation")

main()        
