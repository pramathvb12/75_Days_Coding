# Merge sort
# The time complexity of the merge sort algorithm is O(n log n)
# The space complexity of the merge sort algorithm is O(n)
def merge_sort(arr):
    #Check if array size is gerater than 1
    if len(arr)>1:
        mid = len(arr)//2
        # store left part of array
        left_arr = arr[:mid]
        #store right part of array
        right_arr = arr[mid:]
    
        #recursive call (divide and conquare)
        merge_sort(left_arr)
        merge_sort(right_arr)
        # to track index
        i=j=k=0
        # merging array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        
        #if any element left in left array 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        #if any element left in right array 
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        
arr = [3,1,4,9,3,0,2,6,7,90,45,33,12]

merge_sort(arr)
    
print(arr)

'''
Quick sort

The time complexity of the quicksort algorithm is O(n log n) on average, but it can degrade to O(n^2) in the worst case
The space complexity of quicksort is O(log n) on average, as the algorithm uses a recursive approach and the maximum depth of the recursion is log n

'''
def quick_sort(arr,left,right):
    #check left index less than right
    if left<right:
        #to get partition index for quick sort
        partition_position  = partition(arr,left,right)
        #create left sub array
        quick_sort(arr,left,partition_position-1)
        #create right subarray
        quick_sort(arr,partition_position+1,right)
               
def partition(arr,left,right):
    #first index move right side
    i = left
    #moves left side of array
    j = right - 1
    #last element
    pivot = arr[right]
    
    while i<j:
        #move right pointer
        while i<right and arr[i] < pivot:
            i+=1
        #move left pointer until meets the pivot
        while j>left and arr[j] >= pivot:
            j-=1
        #swap it
        if i<j:
            arr[i],arr[j] = arr[j], arr[i]
    #swap if array element is greater than pivot        
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    #return index
    return i

arr=[22,11,5,78,22,34,88,91,13]
quick_sort(arr,0,len(arr)-1)
print(arr)

'''
Insertion sort
Time complexity  O(n^2) , simple algo
'''
def insertion_sort(arr):
    #iterate through array outer loop
    for i in range(1,len(arr)):
        j=i
        #inner loop
        while arr[j-1] > arr[j] and j>0:
            #swap 
            arr[j-1],arr[j] = arr[j], arr[j-1]
            #decrement
            j-=1
            
arr = [2,6,5,1,8,0,2]
insertion_sort(arr)
print(arr)

'''
Selection sort
Time complexity  O(n^2) , simple algo
'''

def selction_sort(arr):
    #iterate through outer array
    for i in range(0,len(arr)-1):
        #set first element as min
        cur_min = i
        for j in range(i+1,len(arr)):
            # if current element is less than min
            if arr[j] < arr[cur_min]:
                cur_min=j
        #swap
        arr[i],arr[cur_min] = arr[cur_min],arr[i]
 
arr =[2,6,5,3,4,0]
selction_sort(arr)
print(arr)

'''
Bubble sort
swapping 
The time complexity of the bubble sort algorithm is O(n^2) in the worst and average cases, and O(n) in the best case

'''

def bubble_sort(arr):
    #iterate through outer array
    for i in range(len(arr)):
        #iterate through inner array
        for j in range(0,len(arr)-i-1):
            #compare the adjacent elements
            if arr[j]>arr[j+1]:
                #swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
arr = [2,6,5,3,4,0]
bubble_sort(arr)
print(arr) 
