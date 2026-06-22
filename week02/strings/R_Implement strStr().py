'''
Q. 가장 먼저 등장하는 공통부분(needle) 위치 찾기
A.
    => 공통부분이 주어졌으므로 for문 탐색으로 인덱스 슬라이싱해서 찾으면 Easy
    => 근데 복잡하게 풀어버림,,
    1. haystack에 위치한 needle의 첫문자 위치 모두 저장(starts)
    2. 저장된 위치가 없으면 -1
    3. 해당 위치에서 needle이 존재할 수 없으면 -1
    4. 시작점부터 모든 문자가 needle과 일치하면 해당 위치 return
    5. 모든 위치 탐색했을때 답이 없으면 -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        starts = []
        for i,v in enumerate(haystack):
            if v == needle[0]:
                starts.append(i)
        
        if len(starts) == 0: return -1
        
        for s in starts:
            if s + len(needle) > len(haystack):
                return -1
            for i in range(len(needle)):
                if needle[i] != haystack[s+i]:
                    break
                if i == len(needle)-1: return s
        return -1
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1