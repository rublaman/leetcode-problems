# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []

        for i in nums:
            if not i in res:
                res.append(i)

        return len(res)


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
