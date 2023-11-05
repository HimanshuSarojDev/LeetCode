class Solution(object):
    def twoSum(self, nums):
        return nums[1:-1]

       
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums)
if result:
    print(result)  