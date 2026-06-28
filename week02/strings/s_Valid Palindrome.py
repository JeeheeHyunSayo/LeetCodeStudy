class Solution:
    '''
        문자열 전처리 후에 회문 비교하기 
        s.isalpha() : 알파벳 여부, s.isdigit() : 숫자 여부 
    '''
    def isPalindrome(self, s: str) -> bool:
        re_s = ''.join([c.lower() for c in s if c.isalpha() or c.isdigit()])
        return re_s == re_s[::-1]
        