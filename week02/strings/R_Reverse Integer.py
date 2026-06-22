'''
Q. 숫자 뒤집기 + 부호 고려하기
A.
    1. x의 부호 확인 후 절댓값 기준으로 뒤집기
    2. 뒤집힌 값 rev가 범위 밖이면 0
    3. 범위 이내면 부호 고려하여 +/-rev
'''

class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        x = abs(x)
        rev = int(str(x)[::-1])
        if rev > 2**31-1:
            return 0
        else: 
            if neg: return -rev
            return rev