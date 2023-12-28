'''
printing the alternative element in the array
'''
list = [5,6,7,8,9]

for i in range(0,len(list),2):
    print(list[i],end=" ")
    
# Output 5 7 9


'''
Find the count of the smallest elements in the given array which are smaller than given big number.
'''
def count_small(arr,x):
    count=0
    small = []
    
    for num in arr:
        if num<x:
            count+=1
            small.append(num)
    return small,count
    
small, c = count_small(arr=[5,7,8,1,10,45,2,4,15], x=18)
print(f"the smallest elements count is {c} and are : {small}")

#the smallest elements count is 8 and are : [5, 7, 8, 1, 10, 2, 4, 15]

'''
Count Squares
'''
def count_sqaure(n):
    count = 0
    for i in range(1,n):
        if i*i < n:
            count +=1
            
    return count
    
r = count_sqaure(n=130)
print(f"the count of perfect squares is {r}")

#the count of perfect squares is 11

'''
Perfect Numbers
'''
def perfect_num(n):
    count=[]
    s=0
    for i in range(1,n):
        if n%i ==0:
            count.append(i)
        else:
            continue
    s = sum(count)
    if s == n:
        return 1
    else:
        return 0
        
t = perfect_num(n=10)
print(t)

#output 0

'''
Sum of Digit is Pallindrome or not

'''
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def sum_of_digits_palindrome(number):
    # Find the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check if the sum is a palindrome
    return is_palindrome(digit_sum)

# Example usage:
input_number = int(input("Enter a number: "))
result = sum_of_digits_palindrome(input_number)

if result:
    print(f"The sum of digits of {input_number} is a palindrome.")
else:
    print(f"The sum of digits of {input_number} is not a palindrome.")
#palindrome

