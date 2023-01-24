# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        res = []

        if k == 1:
            for i in nums:
                aux = i

        else:
            for i in nums:
                print(i)


solution = Solution()
solution.topKFrequent([1, 1, 1, 2, 2, 3], 1)
