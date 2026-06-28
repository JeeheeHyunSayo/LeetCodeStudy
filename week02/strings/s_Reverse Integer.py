class Solution:
    def reverse(self, x: int) -> int:
        '''
            -2**31 보다 작거나 2**31-1 보다 크면 0 return 조건 까먹음 
        '''
        rev_num = int(str(x)[::-1].replace('-',''))
        if x < 0:
            rev_num = -rev_num
            
        if rev_num < -2**31 or rev_num > 2**31 - 1:
            return 0 
        return rev_num
        