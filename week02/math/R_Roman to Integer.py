'''
Q. 로마자 <-> 10진수
A. 
    1. 각 로마자에 대응하는 10진수 값 맵 생성
    2. 주어진 문자를 역순으로(=작은 값부터) 계산
        2-1. 문자가 뒤보다 작으면 --
        2-2. 문자가 뒤보다 크면 ++
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # res = 0
        # for i in range(len(s)):
        #     if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        #         res -= roman[s[i]]
        #     else:
        #         res += roman[s[i]]
       
        res = roman[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res