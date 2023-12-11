'''
BFS - uses queue ds
maximum flow in the network ,
shortest path finding

time complexity O(V+E), O(n), 
space complexity O(1)

'''
def bfs(graph,startNode):
    #initialise list for storing visited vertex
    visit_node = []
    #use queue ds
    queue = [startNode]
    # start iteration
    while queue:
        #pop node from queue
        cur_node = queue.pop(0)
        #place vertex in visited
        visit_node.append(cur_node)
        #finding neighbour
        for neighbour in graph[cur_node]:
            #not present in visit_node
            if neighbour not in visit_node:
                #add into queue
                queue.append(neighbour)
    return visit_node
#use dictonary for graph vertex,edges   
graph = {
    '0' : ['3','5','9'],
    '1' : ['6','7','4'],
    '2' : ['10','5'],
    '3' : ['0'],
    '4' : ['1','5','8'],
    '5' : ['2','0','4'],
    '6' : ['1'],
    '7' : ['1'],
    '8' : ['4'],
    '9' : ['0'],
    '10': ['2']
}

res = bfs(graph,'0')
print(res)
# Output     ['0', '3', '5', '9', '2', '4', '10', '1', '8', '6', '7']


'''
DFS - uses stack (recursion)

The time complexity of Depth-First Search (DFS) is O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

'''

graph = {
    '0' : ['3','5','9'],
    '1' : ['6','7','4'],
    '2' : ['10','5'],
    '3' : ['0'],
    '4' : ['1','5','8'],
    '5' : ['2','0','4'],
    '6' : ['1'],
    '7' : ['1'],
    '8' : ['4'],
    '9' : ['0'],
    '10': ['2']
}

visited_node =set()

def dfs(node):
    if node not in visited_node:
        print(node, end=" ")
        visited_node.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)
            
dfs('0')

#Output     ['0', '3', '5', '9', '2', '4', '10', '1', '8', '6', '7']


'''
Preorder
Preorder traversal is a tree traversal algorithm that visits the root node first, then recursively performs a preorder traversal of the left subtree, and finally, a preorder traversal of the right subtree.

'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)
        

# Example usage
# Construct a binary tree
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)

# Perform preorder traversal
print("Preorder Traversal:")
preorder_traversal(root)
# Output - 10 8 7 9 12 


'''
Inorder - 
Left Subtree: First, visit all the nodes of the left subtree in an inorder manner.
Root: Visit the root node.
Right Subtree: Finally, visit all the nodes of the right subtree in an inorder manner.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node is not None:
        
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)
        

# Example usage
# Construct a binary tree
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)

# Perform inorder traversal
print("Inorder Traversal:")
inorder_traversal(root)
#Output - 7 8 9 10 12

'''
Postorder -
Left Subtree: First, visit all the nodes of the left subtree in a postorder manner.
Right Subtree: Next, visit all the nodes of the right subtree in a postorder manner.
Root: Finally, visit the root node.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is not None:
        
        postorder_traversal(node.left)
        print(node.value, end=' ')
        postorder_traversal(node.right)
        

# Example usage
# Construct a binary tree
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)

# Perform postorder traversal
print("Postorder Traversal:")
postorder_traversal(root)

# output - 7 9 8 12 10 