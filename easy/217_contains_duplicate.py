# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(nums: list[int]) -> bool:

        if len(set(nums)) != len(nums):
            return True

        return False
