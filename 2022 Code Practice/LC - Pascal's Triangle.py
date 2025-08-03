
"""
Runtime: 37 ms, faster than 67.27% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.8 MB, less than 69.23% of Python3 online submissions for Pascal's Triangle.
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        array = [[1]]
        for l in range(1, numRows):
            lastArray, tempRow = [0] + array[-1] + [0], []
            for r in range(len(array[-1])+1):
                tempRow.append(lastArray[r]+lastArray[r+1])
            array.append(tempRow)
        return array
