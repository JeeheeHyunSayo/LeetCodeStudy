'''
Q. 주어진 문자열들의 가장 긴 prefix 찾기
A. 
    1. 문자열 길이순 정렬
    2. 가장 짧은 문자열을 기준으로 공통 prefix 탐색
    3. 공통부분이 짧아지면 res 갱신
    4. 공통부분이 없어지면 "" return
    5. 마지막에 남은 res return
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        res = strs[0]
        for st in strs[1:]:
            if len(res) == 0: return ""
            for i in range(len(res)):
                if res[i] != st[i]:
                    res = res[:i]
                    break
            # temp = ""
            # for x, y in zip(res, st):
            #     if x == y:
            #         temp += x
            #     else:
            #         break
            # res = temp
            # if len(res) == 0: return ""
        return res