'''
Q. 중복되지 않는 문자 중 제일 먼저 등장하는 값의 위치
A.
    1. 해시테이블 생성(처음 등장하면 인덱스, 두번 이상 등장 시 -1)
    2. 해시테이블 중 값이 -1이 아니면서 가장 작은 수 반환
    3. 모든 해시테이블값이 -1이면 -1 반환
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        for i, v in enumerate(s):
            if v in cnt:
                cnt[v] = -1
            else:
                cnt[v] = i
        
        res = 10**5
        for k, v in cnt.items():
            if v != -1 and res > v:
                res = v
        return res if res != 10**5 else -1