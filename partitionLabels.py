"""

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitionList = []
        i = 0
        while i<len(S):
          startIndex = i
          endIndex = S.rfind(S[i])
          j = startIndex + 1
          while j <= endIndex-1:
            if S.rfind(S[j]) > endIndex:
              endIndex = S.rfind(S[j])
            j+=1
          partitionList.append(endIndex-startIndex+1)
          i = endIndex + 1

        return partitionList
