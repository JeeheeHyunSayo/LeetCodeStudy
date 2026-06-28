class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ''' 
            첫 글자를 기준점으로 삼아서 첫 글자의 글자 조각들을 다른 문자열과 비교하기
        ''' 
        prefix = ''
        first = strs[0] # 기준점
        
        for i in range(len(first)): 
            ch = first[i] 
            for word in strs: 
                if i >= len(word) or word[i] != ch: 
                    return prefix
            prefix += ch 
            
        return prefix 