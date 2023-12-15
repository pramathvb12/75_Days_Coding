# Removing duplicate elements form array using set

list_a = [2,2,1,3,4,5,5,6,1,2]

list_b = set(list_a)

print(list_b)

#iterative way

list_a = [2,2,1,3,4,5,5,6,1,2]

list_b = []

for num in list_a:
    if num not in list_b:
        list_b.append(num)

print(sorted(list_b))


'''
Count number of substring in the given string 
'''
str = "Hello hello hello , Who are you?"

substr = "Hello"

num = str.count(substr.lower())

print(num)

