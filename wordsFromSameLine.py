"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution:
    def findWords(self, words):
      """
      :type words: List[str]
      :rtype: List[str]
      """
      rows, res = {0: 'qwertyuiop', 1: 'asdfghjkl', 2: 'zxcvbnm'}, []
      for word in words:
        for i in range(3):
          valid = ''.join([x for x in list(word) if x.lower() in rows[i]])
          if word == valid:
            res.append(word)
            break
      return res
