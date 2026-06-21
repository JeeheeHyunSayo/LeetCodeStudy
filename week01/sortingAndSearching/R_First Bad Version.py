'''
Q: 배열 중 가장 먼저 등장하는 bad 위치 찾기
A: left, right, mid 비교하는 문제 (근데 문제 설명 이상함)
    1. 초기 left, right를 0, n으로 설정 후 좌우 탐색
    2. Bad는 오른쪽에 존재하므로 isBadVersion 값이 true면 오른쪽 범위 줄이기, false면 왼쪽 줄이기
    3. left == right이면 탐색 종료
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left