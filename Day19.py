#find square root without using builtin methods

def find_sqrt(num):
    if n<2:
        return n
    low,high=1,n
    
    while(low<=high):
        mid = (low+high)//2
        
        if mid*mid == n:
            return mid
        elif mid*mid<n:
            low=mid+1
        else:
            high=mid-1
    return high

n=4
r = find_sqrt(n)
print(f"square root of {n} is : {r}")
#output : 2

#sum of the array

lis = [1,2,3,4,5]

sum =0
for num in lis:
    sum+=num
    

print(f"sum is {sum}") #15

#prime number
def isprime(num):
    if num < 2:
        print("not prime")
        return
    
    for i in range(2, num//2 + 1):
        if num % i == 0:
            print("not prime")
            return
    
    print("prime")

isprime(num=3)  #prime

#swapping two number without third variable
#swap two num

def swap(num1,num2):
    num1,num2=num2,num1
    print(f"After swapping num1:{num1}, num2:{num2}")
    
num1=13
num2=20

print(f"Before swapping num1:{num1}, num2:{num2}")
swap(num1,num2)
# Before swapping num1:13, num2:20
# After swapping num1:20, num2:13

#count of vowels and consonents in the given string

def count(string):
    vc=cc=0
    string.lower()
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vc+=1
        else:
            cc+=1
    return vc,cc
    
vc,cc = count(string="aiouhnhkuji6ere4gtquediditwueww")

print(f"count of vowel is : {vc} and count of consonent is : {cc}")
#count of vowel is : 14 and count of consonent is : 17

#palindrome
def checck_pali(string):
    rev=""
    for i in range(len(string)-1,-1,-1):
        rev+=string[i]
        
  
    if string == rev:
        print("palindrome")
    else:
        print("not palindrome")

checck_pali(string="aoioa")     #palindrome

'''
finding the second largest element 
'''
lis = [3,5,1,0,9,7,19,13]


for i in range(0,len(lis)):
    for j in range(0,len(lis)-i-1):
        if lis[j]> lis[j+1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
            
print(lis[len(lis)-2])  #13
