'''
How do you find all pairs of an integer array whose sum is equal to a given number
'''
lis = [1,2,3,8,6,5,3,4,1]

sum = 9
#for outer loop take from first place
for i in range(0,len(lis)):
    #inner loop take after index of i
    for j in range(i,len(lis)):
        #these two number sum is target
        if lis[i]+lis[j] == sum:
            print(f"pair of sum of taget at {i,j} is :{lis[i],lis[j]}")

#output
# pair of sum of taget at (0, 3) is :(1, 8)
# pair of sum of taget at (2, 4) is :(3, 6)
# pair of sum of taget at (3, 9) is :(8, 1)
# pair of sum of taget at (4, 6) is :(6, 3)
# pair of sum of taget at (5, 8) is :(5, 4)
# pair of sum of taget at (7, 8) is :(5, 4)

'''
How do you search a target value in a rotated array
'''

#to rotate the array
lis = [1, 2, 3, 8, 6, 5, 3, 5, 4, 1]
rotated_list = lis.copy()  # Create a copy of the original list

for i in range(len(lis)):
    rotated_list[i] = lis[(i - 1) % len(lis)]

print(rotated_list)

#set the key to search
key = 5
#search for the element
for i in range(len(lis)):
    if lis[i] == key:
        print(f"item found in {i} : {lis[i]}")

#output
# [1, 1, 2, 3, 8, 6, 5, 3, 5, 4]
# item found in 5 : 5
# item found in 7 : 5

'''
binary search
'''
lis = [2, 5, 7, 8, 1, 10, 9, 78, 90]
key = 98
#set first pointer to first index
i = 0
#last index of array
j = len(lis) - 1
# i is less than j length
while i <= j:
    mid = (i + j) // 2  #  calculation of mid 

    if key == lis[mid]: #item found in mid
        print(f"Item found at index {mid}: {lis[mid]}")
        break
    
    elif key < lis[mid]:    #item is less than mid
        j = mid - 1  # Update the value of j

    elif key > lis[mid]: #item greater than mid
        i = mid + 1  # Update the value of i

    else:
        print("No item")

# If the while loop completes without finding the item, print a message
else:
    print("Item not found in the list")

'''
How to convert a byte array to String
'''
# Create a byte array
byte_array = b'Hello, World!'

# Convert the byte array to a string using the decode method
string_result = byte_array.decode('utf-8')  # 'utf-8' is a common character encoding

# Print the result
print(string_result)

'''
How to find a median of two sorts arrays
for odd length middle is median
for even length (middle-1 + middle)/2
'''
lis = [2, 5, 1, 2, 3, 45, 87, 2, 34, 56, 13]
lis1 = [9, 4, 10, 20, 32, 49, 82, 28, 38, 50, 73]

# Merge the lists and sort the merged list
lis2 = sorted(lis + lis1)

# Calculate the median
mid = len(lis2) // 2
if len(lis2) % 2 == 0:  # Check if the length is even
    median = (lis2[mid - 1] + lis2[mid]) / 2
else:
    median = lis2[mid]

print(lis2)
print(f"Median of lis2 is {median}")

#output
# [1, 2, 2, 2, 3, 4, 5, 9, 10, 13, 20, 28, 32, 34, 38, 45, 49, 50, 56, 73, 82, 87]
# Median of lis2 is 24.0

'''
How to rotate an array left and right by a given number K
'''
lis = [3, 6, 1, 2, 8, 9, 3, 4, 7]
k = 3

# Function to rotate the array to the left by k positions
def rotate(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than the length of the array

    # Slice the array and concatenate the two parts after rotation
    rotated_array_left = arr[k:] + arr[:k] #rotate by left
    rotated_array_right = arr[-k:] + arr[:-k]   #rotate by right
    print("Rotated left Array:", rotated_array_left)
    print("Rotated right Array:", rotated_array_right)
    
# Print the original and rotated arrays
print("Original Array:", lis)
rotate(lis,k)

#output
# Original Array: [3, 6, 1, 2, 8, 9, 3, 4, 7]
# Rotated left Array: [2, 8, 9, 3, 4, 7, 3, 6, 1]
# Rotated right Array: [3, 4, 7, 3, 6, 1, 2, 8, 9]

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence
'''
def longest_consecutive_sequence(nums):
    if not nums:    #number is not in array
        return 0

    num_set = set(nums) #create a ordered set 
    max_length = 0

    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Increment current_num and current_length for consecutive elements
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(nums)
print(f"The length of the longest consecutive sequence is: {result}")
# uutput : 4 i.e 1,2,3,4

'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given value
'''
lis = [2, 2, 4, 4, 4, 6, 8, 9, 9]
key = 4

starting_point = None

for i in range(len(lis)):
    if lis[i] == key:
        starting_point = i
        break

if starting_point is not None:
    ending_point = starting_point

    for i in range(starting_point + 1, len(lis)):
        if lis[i] == key:
            ending_point = i
        else:
            break

    print(f"Starting point is: {starting_point}")
    print(f"Ending point is: {ending_point}")
else:
    print(f"The key {key} is not present in the array.")
#output    
# Starting point is: 2
# Ending point is: 4   


'''
Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum
'''
#kadanes algorithm

def max_subarray_sum(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # Choose the maximum between the current element and the sum ending at the previous element
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums =  [2, 2, 4, 4, 4, 6, 8, 9, 9,4,6,8,1]
result = max_subarray_sum(nums)
print(f"The maximum subarray sum is: {result}")










        