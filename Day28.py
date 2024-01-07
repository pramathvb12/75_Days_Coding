'''
Chef is fan of pairs and he likes all things that come in pairs. He even has a doll collection in which the dolls come in pairs. One day while going through his collection he found that there are odd number of dolls. Someone had stolen a doll!!!

Help chef find which type of doll is missing..

Input
The first line contains an integer T, the number of test cases.
The first line of each test case contains an integer N, the number of dolls.
The next N lines are the types of dolls that are left.

Output
For each test case, display the type of doll that doesn't have a pair, in a new line.

Constraints
1<=T<=10
1<=N<=100000 (10^5)
0<=type<=100000
'''
def find_missing_doll_type():
    # Number of test cases
    t = int(input())

    for _ in range(t):
        # Number of dolls in the current test case
        n = int(input())

        # Initialize a dictionary to store the count of each doll type
        doll_count = {}

        # Read the types of dolls and update the count in the dictionary
        for _ in range(n):
            doll_type = int(input())
            doll_count[doll_type] = doll_count.get(doll_type, 0) + 1

        # Find the doll type with an odd count (the missing doll)
        for doll_type, count in doll_count.items():
            if count % 2 != 0:
                print(doll_type)
                break

# Example usage
find_missing_doll_type()

'''
You are given an array 
�
A of size 
�
N. In one operation, you can do the following:

Select indices 
�
i and 
�
j 
(
�
≠
�
)
(i=j) and set 
�
�
=
�
�
A 
i
​
 =A 
j
​
 .
Find the minimum number of operations required to make all elements of the array equal.

Input Format
The first line of input will contain a single integer 
�
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer 
�
N — the size of the array.
The next line contains 
�
N space-separated integers, denoting the array 
�
A.
Output Format
For each test case, output on a new line, the minimum number of operations required to make all elements of the array equal.

Constraints
1
≤
�
≤
1000
1≤T≤1000
1
≤
�
≤
2
⋅
1
0
5
1≤N≤2⋅10 
5
 
1
≤
�
�
≤
�
1≤A 
i
​
 ≤N
The sum of 
�
N over all test cases won't exceed 
2
⋅
1
0
5
2⋅10 
5
 .
'''
def min_operations_to_equalize_array(arr):
    n = len(arr)
    
    # Count occurrences of each element
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Find the maximum occurrence
    max_occurrence = max(count.values())
    
    # Minimum operations needed is the total number of elements minus the maximum occurrence
    min_operations = n - max_occurrence
    
    return min_operations

def main():
    # Number of test cases
    t = int(input())
    
    for _ in range(t):
        # Size of the array
        n = int(input())
        
        # Array elements
        arr = list(map(int, input().split()))
        
        # Output the result for each test case
        print(min_operations_to_equalize_array(arr))

# Example usage
main()

