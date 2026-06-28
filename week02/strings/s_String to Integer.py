class Solution:
    def myAtoi(self, s: str) -> int:
        '''
            첫 단어가 부호(+/-) 인지 확인 
            s.isdigit() : 숫자만 추가 
        '''
        i = 0 
        n = len(s) 
        
        while i < n and s[i] == ' ': 
            i += 1 
        
        sign = 1 
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1 
            i += 1 
        
        str_num = '' 
        while i < n and s[i].isdigit(): 
            str_num += s[i] 
            i += 1 
        
        if str_num == '':
            return 0 
        
        num = sign * int(str_num) 
        
        if num < -2**31:
            num = -2**31
        elif num > 2**31 -1:
            num = 2**31 - 1 
        
        return num 
        
        