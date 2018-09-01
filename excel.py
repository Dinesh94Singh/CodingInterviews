# In Excel rows start with A and go on till AA and AAA and so on.
# A - 1
# B - 2
# Z - 26
# ...
# ...
# ...
# AA - 27
# AB - 28
# ...
# AAA - 703

class Solution:
    def determineRowNumber(s):
        d = {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5,
            'F' : 6,
            'G' : 7,
            'H' : 8,
            'I' : 9,
            'J' : 10,
            'K' : 11,
            'L' : 12,
            'M' : 13,
            'N' : 14,
            'O' : 15,
            'P' : 16,
            'Q' : 17,
            'R' : 18,
            'S' : 19,
            'T' : 20,
            'U' : 21,
            'V' : 22,
            'W' : 23,
            'X' : 24,
            'Y' : 25,
            'Z' : 26
        }

        c = len(s) - 1
        sum = 0
        for i in s:
            sum = sum + d [i] * 26**c
            c = c - 1
        return sum