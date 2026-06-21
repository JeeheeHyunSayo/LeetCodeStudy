'''
Q: 2D matrix 시계방향 90도 회전시키기
A:
    zip 쓰면 바로 풀리는 삼전코테St 문제... (=배열 역으로 뒤집고[::-1] 분해해서* Zip으로 묶는 구조)
    1. 배열을 역순으로 뒤집고
    2. 대각선 위쪽에 있는 값 기준 축대칭으로 뒤집기
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = [list(a) for a in zip(*matrix[::-1])]
        # matrix[:] = zip(*matrix[::-1]) # 이렇게 풀면 됨!
        m = len(matrix)
        for i in range(m//2):
            matrix[i], matrix[m-i-1] = matrix[m-i-1], matrix[i]
        
        for i in range(m):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]