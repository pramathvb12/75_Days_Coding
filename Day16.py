'''
How do you find the missing number in a given integer array of 1 to 100

'''
#solution
list = [1,2,3,4,5,6,8,9,10]
n=10
expected_sum = n*(n+1)//2

existing_sum =0

for num in list:
    existing_sum+=num
    
missing_num = expected_sum - existing_sum
print(missing_num)

# output 7

'''
How do you find the duplicate number on a given integer array
'''
my_list = [2, 3, 4, 5, 2, 6, 4, 8, 9]
#create a set for non duplicate element
unique_set = set()
dup = []

for num in my_list:
    if num in unique_set:
        dup.append(num)
    else:
        unique_set.add(num)

print(dup)


#output 2,4

'''
How do you find the largest and smallest number in an unsorted integer array
'''
#using built in method
my_list = [2, 3, 4, 5, 2, 6, 4, 8, 9]
print(min(my_list))
print(max(my_list))

#or

my_list = [2, 3, 4, 5, 2, 6, 4, 8, 9]
mini = float('inf')
maxi = float('-inf')  # Initialize maxi with negative infinity

for num in my_list:
    if num > maxi:
        maxi = num
    if num < mini:
        mini = num

print(mini, maxi)

#or
my_list = [2, 3, 4, 5, 2, 6, 4, 8, 9]
mini = my_list[0]
maxi = my_list[0]  # Initialize maxi with first

for num in range(1,len(my_list)):
    if my_list[num] > maxi:
        maxi = my_list[num]
    if my_list[num] < mini:
        mini=my_list[num]
        
print(mini,maxi)

#or 
my_list = [2, 3, 4, 5, 2, 6, 4, 8, 9]
sorted(my_list)
mini = my_list[0]
maxi = my_list[len(my_list)-1] # Initialize maxi with first

print(mini,maxi)

#output 2 9

'''
How to remove duplicates from a given array 
'''
list = [2,7,8,1,2,4,4,5,7,10]
lis = []
# iterative approach
for num in list:
    if num not in lis:
        lis.append(num)
#using built-in set
lis1 = set(list)

print(lis)
print(lis1)

#[2, 7, 8, 1, 4, 5, 10]
#{1, 2, 4, 5, 7, 8, 10}

'''
How do you reverse an array
'''
#iterative way
lis = [1, 2, 3, 4, 8, 9, 0]
lis1 = []
#start from the last index
for i in range(len(lis)-1, -1, -1):
    lis1.append(lis[i])

print(lis1)

#builtin way

print(lis[::-1])





