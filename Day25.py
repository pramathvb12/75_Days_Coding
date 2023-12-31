'''
Finding the given sum in the subarray
'''
def find_sum(arr,sum):
    dict ={}
    cur_sum=0
    
    for i in range(len(arr)):
        cur_sum+=arr[i]
        
        if cur_sum == sum:
            print("sub array starts from 0 to",i)
            break
        if cur_sum - sum in dict:
            print("sub array starts from",dict[cur_sum - sum]+1,"to",i)
            break
        dict[cur_sum]=i
    else:
        print("no subarray")
    
        
find_sum(arr=[10,2,-2,-20,-10],sum=-10)

#sub array starts from 0 to 3

#maximum subarray using O(n)

def find_max(arr):
    maxsub=0
    cur = 0
    
    for num in arr:
        if cur<0:
            cur=0
        cur+=num
        maxsub = max(cur,maxsub)
        
    return maxsub
    
r = find_max(arr=[-2,1,-3,4,-1,2,1,-5,4])
print(r)
# output 6


'''
To print index subarray
'''
def find_max_subarray(arr):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    cur_sum = 0
    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i, num in enumerate(arr):
        if cur_sum < 0:
            cur_sum = 0
            temp_start_index = i

        cur_sum += num

        if cur_sum > max_sum:
            max_sum = cur_sum
            start_index = temp_start_index
            end_index = i

    return max_sum, start_index, end_index

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = find_max_subarray(arr)
print("Maximum Subarray Sum:", result[0])
print("Start Index:", result[1])
print("End Index:", result[2])
