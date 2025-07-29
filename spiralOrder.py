# 54. Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
