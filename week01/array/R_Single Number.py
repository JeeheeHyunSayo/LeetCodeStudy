'''
Q: 리스트 내에서 유일하게 중복되지 않는 값 반환하기
A: 
    1. 딕셔너리에 항목 저장
    2. 중복 시 딕셔너리 항목 제거
    3. 최후에 딕셔너리에 남은 키값 반환
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numList = {}
        for i in nums:
            if i in numList:
                del numList[i]
            else:
                numList[i] = True
        return list(numList.keys())[0]