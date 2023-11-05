class Solution(object):
        def maxProduct(self, nums):
            nums.sort(reverse=True)  
            max1 = nums[0]-1
            max2 = nums[1]-1
            return max1 * max2


solution = Solution()
nums = [2, 3, 4, 5]
result = solution.maxProduct(nums)
print(result) 