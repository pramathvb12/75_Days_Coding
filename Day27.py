#In the given list of number return the final sum , where sum the positive inndex and negete the odd index.
list1 = [29,87,29]
sum=0
for i in range(len(list1)):
    if i%2 ==0:
        sum+=list1[i]
    else:
        sum-=list1[i]
        
print(abs(sum)) 

#29

'''
Imagine you are working for the local government as a land surveyor. It is your job to find out how much more space there is on the city's current industrial site for new buildings. To that end, you need to measure how many buildings there are today.

The industrial site is represented by a 2D array, where "B" represents (part of) a building and "E" represents empty space. If B's are horizontally or vertically connected to other B's, then those B's are part of one building. If two B's are only diagonally connected, regard them as separate buildings.

Write a function:

find_building(input_map)

that returns the number of buildings on the industrial site. If any of the elements in the array are not "B" or "E", the function should return -1.

Note: the initial code in the editor uses tabs for indentation. Don't mix it with spaces.
There are three buildings in the following example:


There are three buildings in the following example:

Input parameters: ([["B", "B", "B"], ["B", "Ε", "B"], ["E", "E", "E"], ["E", "E", "B"], ["B", "E", "B"],])


Expected: (3,)

For this test you're using Python 3.8

Feel free to add comments in your code explaining your solution.
'''
def find_building(input_map):
    # Check if input_map is a valid 2D array
    if not all(isinstance(row, list) and all(isinstance(cell, str) for cell in row) for row in input_map):
        return -1

    building_count = 0

    # Function to perform depth-first search (DFS) to mark connected buildings
    def dfs(row, col):
        stack = [(row, col)]

        while stack:
            current_row, current_col = stack.pop()

            if 0 <= current_row < len(input_map) and 0 <= current_col < len(input_map[0]) and input_map[current_row][current_col] == "B":
                input_map[current_row][current_col] = "V"  # Mark the cell as visited
                stack.extend([(current_row + 1, current_col), (current_row - 1, current_col), (current_row, current_col + 1), (current_row, current_col - 1)])

    # Iterate through the 2D array
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == "B":
                building_count += 1
                dfs(i, j)  # Mark connected buildings using iteration

    return building_count

# Example usage:
input_map = [["B", "B", "B"], ["B", "E", "B"], ["E", "E", "E"], ["E", "E", "B"], ["B", "E", "B"]]
result = find_building(input_map)
print(result)
# 3