class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
            딕셔너리를 활용하여 문자열 s의 알파벳 카운트를 저장 -> 한 번 나온 알파벳의 인덱스를 반환 
        '''
        cnt_dict = {} 
        for word in s: 
            if word in cnt_dict:
                cnt_dict[word] += 1 
            else:
                cnt_dict[word] = 1
        for i, ch in enumerate(s):
            if cnt_dict[ch] == 1:
                return i 
        return -1