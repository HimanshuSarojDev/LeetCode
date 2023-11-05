class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}  

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
if result:
    print(result)  # Output: [0, 1]
