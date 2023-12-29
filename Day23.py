def max_subarray(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to zero

    start_index = 0  # Initialize start_index of the current subarray
    end_index = 0  # Initialize end_index of the current subarray
    temp_start_index = 0  # Temporary start_index to track the beginning of the potential new subarray

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

        if current_sum < 0:
            current_sum = 0
            temp_start_index = i + 1

    return nums[start_index:end_index + 1]

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print("Maximum Subarray:", result)
