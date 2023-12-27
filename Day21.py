'''
sort given two array and merge it
'''
def arr_sort(list1,list2):
    li = []
    li = sorted(list1)
    lii=sorted(list2)
    lo =  list(li+lii)
    
    for i in range(0,len(lo)):
        for j in range(0,len(lo)-i-1):
            if lo[j]>lo[j+1]:
                lo[j],lo[j+1] = lo[j+1],lo[j]
    return lo
    
l = arr_sort(list1=[4,1,2,0,3],list2=[9,3,6,4,1])
print(l)
#[0, 1, 1, 2, 3, 3, 4, 4, 6, 9]

'''
find even or odd given number
'''
def ev_odd(n):
    if n<0:
        print("enter correct num")
    if n %2 ==0:
        print("even")
    else:
        print("Odd")
        
ev_odd(5)
#Odd

'''
count number of even and odd in given array
'''
def ev_odd_count(lis):
    ec=oc=0
    for num in lis:
        if num < 0:
            continue
        elif num %2 == 0:
            ec+=1
        else:
            oc+=1
    return ec,oc
    
ev,oc = ev_odd_count(lis=[6,5,2,1,0,9,-1,3,2,1,6,7,0,-2,7])
print(f"number of even is : {ev} and number of odd : {oc}")
#number of even is : 6 and number of odd : 7

#seperate given array into odd and even
def ev_odd_count(lis):
    even =[]
    odd = []
    for num in lis:
        if num < 0:
            continue
        elif num %2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
    
ev,oc = ev_odd_count(lis=[6,5,2,1,0,9,-1,3,2,1,6,7,0,-2,7])
print(f" even is : {ev} and  odd is: {oc}")
#even is : [6, 2, 0, 2, 6, 0] and  odd is: [5, 1, 9, 3, 1, 7, 7]

#  Write a program to Find the Second Lowest Number.


#finding second smallest number

lis = [2,1,0,4,7,4,6]

li = sorted(lis)
print(li)
print(f"second smallest is {li[1]}")

