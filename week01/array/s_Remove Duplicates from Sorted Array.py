'''
    정렬된 배열에서 중복제거 
    * 요구사항 : 추가 배열을 사용하지 않고 원본 배열을 직접 수정해야함 * 
    * 해결 방법: 
        (1) write = 1, 고유한 원소의 개수 변수 초기화(최소 1개는 고유의 값임)
        (2) 1 ~ len(nums)-1 순회하면서 현재값 <> 이전값 비교 
        (3) 현재값 != 이전값 -> nums[write] 에 현재값을 overwrite 
        (4) write += 1, write 값 갱신 
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write] = nums[i] 
                write += 1 
        return write
        