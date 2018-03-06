'''

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

Link - https://leetcode.com/problems/island-perimeter/description/

'''


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def sum_Adjacent(i,j):
          adjacent_tuples = (i+1, j), (i-1, j), (i, j+1), (i, j-1),
          sum = 0
          for x,y in adjacent_tuples:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
              sum = sum + 1
          return sum
        count = 0
        for i in range(0, len(grid)):
          for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
              count = count + sum_Adjacent(i, j)
        return count