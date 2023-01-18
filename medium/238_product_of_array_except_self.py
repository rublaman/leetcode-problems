# https://leetcode.com/problems/product-of-array-except-self/

'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         res = []

#         for i in range(len(nums)):
#             res.append(1)
#             for j in range(len(nums)):
#                 print(j)
#                 if i != j:
#                     res[i] *= nums[j]

#         return res

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))
