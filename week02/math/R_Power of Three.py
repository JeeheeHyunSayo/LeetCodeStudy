'''
Q. 주어진 수가 3의 제곱수인지 확인
A. 주어진 수가 0 이하이면 false, 그 이상인 경우 반복문을 통해 3으로 나누어떨어지면 true
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        
        while n % 3 == 0:
            n /= 3
        return True if n==1 else False
        
        # without loops
        # x = floor(log(2**31-1)/log(3))
        # if 3**x % n == 0:
        #     return True
        # else: return False