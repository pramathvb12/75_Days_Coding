'''
given digit into word
'''
def number_to_words(number):
    # Define lists for words representation
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Function to convert a three-digit number to words
    def convert_three_digits(num):
        result = ""
        if num >= 100:
            result += units[num // 100] + " hundred "
            num %= 100
        if num >= 20:
            result += tens[num // 10] + " "
            num %= 10
        elif num >= 10:
            return result + teens[num - 10] + " "
        if num > 0:
            result += units[num] + " "
        return result

    # Main function
    if number == 0:
        return "zero"

    result = ""
    if number < 0:
        result = "negative "
        number = abs(number)

    if number >= 1_000_000_000:
        result += convert_three_digits(number // 1_000_000_000) + "billion "
        number %= 1_000_000_000
    if number >= 1_000_000:
        result += convert_three_digits(number // 1_000_000) + "million "
        number %= 1_000_000
    if number >= 1000:
        result += convert_three_digits(number // 1000) + "thousand "
        number %= 1000

    result += convert_three_digits(number).strip()

    return result.strip()

# Example 
number = 123
result = number_to_words(number)
print(result)

'''
Recursion - Function calling itself and has one terminating condition 
'''
#function for factorial of number
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
    
print(fact(n=10))

'''
Binary search tree using recursion
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root
    
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        # if root has key to search
        if root is None or root.key == key:
            return root
        #less means traverse left of tree
        if key < root.key:
            return self._search(root.left, key)
        #else right
        return self._search(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

# Example 
bst = BinarySearchTree()
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    bst.insert(key)

print("Inorder Traversal:", bst.inorder_traversal())

search_key = 40
result = bst.search(search_key)

if result:
    print(f"Key {search_key} found in the BST.")
else:
    print(f"Key {search_key} not found in the BST.")


