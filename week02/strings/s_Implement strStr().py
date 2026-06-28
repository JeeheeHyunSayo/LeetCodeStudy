class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ''' 
            슬라이싱으로 heystack 잘라서 needle 일치 여부 확인 
        '''
        n = len(needle) 
        for i in range(len(haystack)):
            if haystack[i:n+i] == needle: 
                return i 
        return -1