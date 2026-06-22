'''
Q. 두 문자열이 서로의 애너그램인지 확인(=문자열 구성이 똑같은지)
A.
    1. 각 문자열의 길이가 다르면 애너그램 성립X
    2. s를 기준으로 해시테이블 생성
    3. t와 해시테이블 비교; 해시테이블에 없는 문자가 있거나 특정 문자가 더 많이 사용된 경우 false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt = {}
        for i,v in enumerate(s):
            if v in cnt:
                cnt[v] += 1
            else: cnt[v] = 1
        
        for v in t:
            if v in cnt:
                cnt[v] -= 1
                if cnt[v] < 0: return False
            else: return False
        return True