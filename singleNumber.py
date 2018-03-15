'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Referneces: 1) Any number xored with 0 will give the same number
            2) Any number xored with same number will give 0

'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for each in nums:
            res = res ^ each
        return res