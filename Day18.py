# Python3 program to find first non-repeating element.

def firstNonRepeating(arr, n):
	# Loop for checking each element
	for i in range(n):
		j = 0
		# Checking if ith element is present in array
		while(j < n):
			if (i != j and arr[i] == arr[j]):
				break
			j += 1
		# if ith element is not present in array
		# except at ith index then return element
		if (j == n):
			return arr[i]

	return -1

# Driver code
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))

# Output 6

'''
linked list 
'''
#creating the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#function to create      
def create_linked_list():
    first = Node(10)    #first to third node node creation
    second = Node(20)
    third =Node(30)
    
    first.next = second #linking to the next node
    second.next = third
    
    return first    #first node return

def display_ll(head):
    cur = head  #set to start node 
    while cur:
        print(cur.data,end='->')    #print the data
        cur=cur.next
    print('None')   #set last link to None
    
    
head = create_linked_list()
print("linked list is:")
display_ll(head)
#Output
# linked list is:
# 10->20->30->None

'''
Reverse the linked list
'''
#creating the linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# these two functions are similar to above    
def create_linked_list():
    first = Node(10)
    second = Node(20)
    third =Node(30)
    
    first.next = second
    second.next = third
    
    return first

def display_ll(head):
    cur = head
    while cur:
        print(cur.data,end='->')
        cur=cur.next
    print('None')
    
def rev_ll(head):   #function to reverse the ll
    cur=prev=next_node=None
    cur=head    #ste to the first node
    while cur:  #until cur is None
        next_node = cur.next    #set value of next
        cur.next = prev         #store prev to next
        prev = cur
        cur = next_node
    return prev

head = create_linked_list()
print("linked list is:")
display_ll(head)
rev = rev_ll(head)
display_ll(rev)

#output
# linked list is:
# 10->20->30->None
# 30->20->10->None

'''
Finding the middle element in the linked list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow_pointer = head     #set the both pointer to first node
    fast_pointer = head

    while fast_pointer is not None and fast_pointer.next is not None: #while the fast pointer not None
        slow_pointer = slow_pointer.next    #move the slow pointer to one node next 
        fast_pointer = fast_pointer.next.next   #move the fast pointer to two node next

    return slow_pointer.data    # data of slow pointer

def display_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage
def main():
    head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    fifth = Node(50)
    sixth = Node(60)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next =sixth

    print("Original Linked List:")
    display_linked_list(head)

    middle_element = find_middle(head)
    print("Middle Element:", middle_element)

if __name__ == "__main__":
    main()
#output 
# Original Linked List:
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None
# Middle Element: 40


    
    
    

    
    
    