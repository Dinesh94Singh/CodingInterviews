'''

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.

References: 1) First Occurence of a number is odd, 2nd Occurence is even till we encounter a single element.
            2) After the single element, First Occurence is even, 2nd Occurence is odd.
            3) XOR a even number with 1 will give, i+1th pos of that even number.
            4) XOR a odd number with 1 will give, i-1th pos of that even number.
'''


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
          mid = int((low + high)/2)
          if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
          else:
            high = mid
        return nums[low]
          