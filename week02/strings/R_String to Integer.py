'''
Q. 주어진 문자열에서 유효한 숫자열 추출하기
A.
    1. 숫자 시작 지점 파악 (공백 무시, 알파벳 및 '.'은 0 반환, 숫자 또는 +/- 나오면 숫자 시작으로 간주)
    2. 숫자 구역에서(start=True) 숫자 이외 다른 문자 나오면 탐색 종료
    3. 결과물(res)이 존재하는 경우, 값의 범위 및 부호 고려하여 int 값 반환환
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        pos = True
        start = False
        res = ''
        for i in s:
            if start == False:
                if i.isalpha() or i =='.': return 0
                if i == ' ': continue
                start = True
                if i == '-':
                    pos = False
                elif i.isdigit():
                    res += i
            else:
                if i.isdigit():
                    res += i
                else:
                    break

        if len(res) > 0:
            if int(res) <= 2**31-1:
                return int(res) if pos else -int(res)
            if pos == False and int(res) >= 2**31: return -2**31
            if int(res) > 2**31-1: return 2**31-1
        else: return 0