'''
fibonacci series
'''
def fibonacci(n):
    fib_series = [0, 1]
    
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series

n = 10  # You can change this to generate the series up to a different term
result = fibonacci(n)
print(f"Fibonacci series up to term {n}: {result}")

#Fibonacci series up to term 10: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

'''
Remove the occurance given char in string
'''
def r_char(string, c):
    for char in string:
        if char == c:
            string = string.replace(char, '')

    return string

s = r_char(string="thor", c='h')
print(s)
#tor

'''
Count occurances of each char 
'''
def count_occ(string):
    freq = {}
    for x in string:
        freq[x] = freq.get(x,0)+1
        
    return freq
    
t = count_occ("fhujeuehywiherwdwetgrgdsdaaghjyy")
print(t)
print(f"{t.keys()},\n{t.values()},\n{t.items()}")

#{'f': 1, 'h': 4, 'u': 2, 'j': 2, 'e': 4, 'y': 3, 'w': 3, 'i': 1, 'r': 2, 'd': 3, 't': 1, 'g': 3, 's': 1, 'a': 2}

