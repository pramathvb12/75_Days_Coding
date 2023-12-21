'''
permutations of the string
'''
def get_permutations_iterative(input_str):
    n = len(input_str)
    result = [list(input_str)]

    while True:
        # Find the rightmost character that is smaller than the character to its right
        i = n - 2
        while i >= 0 and result[-1][i] >= result[-1][i + 1]:
            i -= 1

        if i == -1:
            # If no such character is found, all permutations are generated
            break

        # Find the smallest character to the right of i and larger than result[i]
        j = n - 1
        while result[-1][j] <= result[-1][i]:
            j -= 1

        # Swap result[i] and result[j]
        result[-1][i], result[-1][j] = result[-1][j], result[-1][i]

        # Reverse the suffix starting at i + 1
        result[-1][i + 1:] = reversed(result[-1][i + 1:])

        # Append a copy of the current permutation to the result
        result.append(result[-1][:])

    # Convert the list of lists to a list of strings
    return [''.join(perm) for perm in result]

# Example 
input_string = "abc"
result = get_permutations_iterative(input_string)

print(f"Permutations of '{input_string}' (iterative):")
for perm in result:
    print(perm)
    
    
'''
substring in given string
'''
s1 = "ggabcdef"
s2 = "gydefswe"
lis = []
lis1 =[]
for i in range(len(s1)-1):
    lis.append(s1[i:i+2])
    lis1.append(s2[i:i+2])
    
print(lis)
print(lis1)

    
'''
Kadane's algorithm - finding maximam sum of subarray in given array
'''
def kadanes_algorithm(nums):
    max_current = max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)

    return max_global

# Example
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(array)
print("Maximum sum subarray:", result)


