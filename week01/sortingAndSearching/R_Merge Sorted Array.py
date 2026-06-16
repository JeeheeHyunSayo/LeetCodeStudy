'''
Q: non-decreasing order 배열 두 개를 non-decreasing order 배열 하나로 합치기
A:
    !포인터 사용!
    1. 각 배열의 유효한 숫자가 존재하는 마지막 인덱스(l1,l2)와 합쳐진 배열의 맨 마지막 인덱스(k)
    2. nums2에 남은 숫자가 없을 때까지 반복(while)
    3. nums1에 아직 유효한 값이 남아있고(l1>=0) 그 값이 nums2보다 클때, k에 nums1[l1] 지정
    4. 그렇지 않은 경우 k에 nums2[l2] 지정
    5. 3-4 모두 값을 지정한 후에는 인덱스 감소(l1-- or l2--) 위치 k도 감소(k--)
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, k = m-1, n-1, m+n-1
        while l2 >= 0:
            if l1 >= 0 and nums1[l1] > nums2[l2]:
                nums1[k] = nums1[l1]
                l1 -= 1
            else:
                nums1[k] = nums2[l2]
                l2 -= 1
            k -= 1