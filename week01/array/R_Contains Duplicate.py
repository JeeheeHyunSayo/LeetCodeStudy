'''
Q: 배열 내 중복값 여부 확인
A: 딕셔너리 생성 후 배열 내 값이 딕셔너리에 이미 존재하면 True
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in nums:
            if i in cnt:
                return True
            else:
                cnt[i] = 1
        return False