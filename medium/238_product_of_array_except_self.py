# https://leetcode.com/problems/product-of-array-except-self/

'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []

        for i in range(len(nums)-1):
            res.append(1)
            for j in range(len(nums)-1):
                if i != j:
                    res[i] *= nums[j]

        return res


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
