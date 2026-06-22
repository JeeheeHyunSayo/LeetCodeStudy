'''
Q. 배열로 주어진 문자열 뒤집기
A:
    - 인덱스 슬라이싱 이용하기
    - 시작과 끝점 포인터 지정해서 값 교환하기
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        # s[:] = s[::-1]