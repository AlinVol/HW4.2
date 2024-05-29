def sum_even_indices_multiply_last(nums):
    if not nums:
        return 0
    even_indices_sum = sum(nums[::2])
    return even_indices_sum * nums[-1]

print(sum_even_indices_multiply_last([0, 1, 7, 2, 4, 8]))
print(sum_even_indices_multiply_last([1, 3, 5]))
print(sum_even_indices_multiply_last([6]))
print(sum_even_indices_multiply_last([]))
