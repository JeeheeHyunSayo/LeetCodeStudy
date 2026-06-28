from collections import Counter
class Solution:
    '''
        collections 모듈 사용해서 풀기 
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s) 
        t_cnt = Counter(t)
        return s_cnt == t_cnt