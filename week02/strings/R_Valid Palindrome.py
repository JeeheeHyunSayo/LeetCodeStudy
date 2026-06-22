'''
Q. 주어진 문자열에서 영문/숫자 부분이 palindrome인지 확인
A.
    1. 아스키코드 기반으로 대문자->소문자, 영/숫자 이외->0 으로 변경
    2. 투 포인터 사용하여 둘 중 하나라도 0이면 pass
    3. 아스키코드가 0이 아닌 경우 값 비교
        3-1. 같으면 다음 문자 비교
        3-2. 다르면 false
    4. 모든 문자열을 비교하여 일치하면 true
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        
        while start < end:
            s1, s2 = self.asciiChange(s[start]), self.asciiChange(s[end])
            if s1 == 0:
                start += 1
            elif s2 == 0:
                end -= 1
            elif s1 == s2:
                start += 1
                end -= 1
            else:
                return False
        return True
    
    def asciiChange(self, s): # lowercase, number
        if 65 <= ord(s) <= 90:
            return ord(s)+32
        if 97 <= ord(s) <= 122 or 48 <= ord(s) <= 57:
            return ord(s)
        else: return 0

s = "a."
print(Solution().isPalindrome(s))