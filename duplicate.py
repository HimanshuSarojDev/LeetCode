class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()  # Use a set to store unique elements
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


solution = Solution()
nums = [1,2,3,4]
result = solution.containsDuplicate(nums)
if result:
    print(result)  