'''

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

Logic: Refer Manachers Algorithm in google ( or )Each element is a palindrome itself, so, think that,

if [a,b] is the range of the palindrome a,a+1,a+2 .... b is a palindrome => a+1,a+2,....b-1 is a palindrome, which means, starting from center left == right where left decrements and right increments.

we expand till left reaches 0 and right reaches N (inclusive) and increment the value when s[left] == s[right]

we are considering 2*N-1 because, each index in a string at different positions can form the center of the palindrome

Trace the program, to understand better
'''


class Solution:
    def countSubstrings(self, S):
        """
        :type s: str
        :rtype: int
        """
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
          left = int(center / 2)
          right = left + int(center % 2)
          while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
        return ans