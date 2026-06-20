'''
Q. n 미만의 소수의 개수
A. 에라토스테네스의 체 이용
    1. n <= 2: 2 미만의 소수는 없음
    2. 소수는 true, 소수가 아닌 수는 false로 하는 배열 생성
    3. 2부터 루트n까지 범위 탐색
        3-1. i가 소수이면 n 미만인 i의 배수는 모두 false
        3-2. i가 소수가 아니면 pass
    4. sum()으로 남아있는 True 개수 세기
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if sieve[i] == True:
                for j in range(i*i, n, i):
                    sieve[j] = False
        
        return sum(sieve) # True=1
        
        # cnt = 0
        # for i in range(n+1):
        #     if sieve[i] == True:
        #         cnt += 1
        # return cnt