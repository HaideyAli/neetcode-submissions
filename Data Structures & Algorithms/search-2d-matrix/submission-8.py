class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mLeft = 0
        mRight = len(matrix) - 1
        while mLeft <= mRight:
            mid = (mLeft + mRight) // 2
            print(mid)
            if matrix[mid][0] <= target:
                mLeft = mid + 1
            else:
                mRight = mid - 1

        row = mRight

        if row < 0:
            return False

        nLeft = 0
        nRight = len(matrix[0]) - 1

        while nLeft <= nRight:
            mid = (nLeft + nRight) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                nLeft = mid + 1
            else:
                nRight = mid - 1
        
        return False